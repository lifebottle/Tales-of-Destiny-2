using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using TalesOfDestinyTm2Converter.Quantizer;
using ttemma.Helpers;

namespace TalesOfDestinyTm2Converter
{
	// Token: 0x02000007 RID: 7
	public class TM2
	{
		// Token: 0x0600003E RID: 62 RVA: 0x00003B2C File Offset: 0x0000272C
		public static TM2 ReadBinary(string fileName)
		{
			TM2 tm = new TM2();
			using (StreamHelper streamHelper = new StreamHelper(fileName, ByteEncoding.Little, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.Read))
			{
				tm.Header = Header.Read(streamHelper);
				tm.PaletteBlocks = new List<PaletteBlock>();
				tm.TextureBlocks = new List<TextureBlock>();
				for (int i = 0; i < (int)tm.Header.CountPalette; i++)
				{
					tm.PaletteBlocks.Add(PaletteBlock.Read(streamHelper));
				}
				for (int j = 0; j < (int)tm.Header.CountTextures; j++)
				{
					tm.TextureBlocks.Add(TextureBlock.Read(streamHelper));
				}
			}
			return tm;
		}

		// Token: 0x0600003F RID: 63 RVA: 0x00003BD8 File Offset: 0x000027D8
		public bool Validate(out string error)
		{
			error = string.Empty;
			if (this.Header.CountTextures > 1)
			{
				error = "Not supported CountTextures more 1";
				return false;
			}
			if (this.Header.CountUnknown > 1)
			{
				error = "Not supported CountUnk more 1";
				return false;
			}
			if (this.Header.CountPalette > 1)
			{
				error = "Not supported CountPalette more 1";
				return false;
			}
			using (List<PaletteBlock>.Enumerator enumerator = this.PaletteBlocks.GetEnumerator())
			{
				while (enumerator.MoveNext())
				{
					if (!enumerator.Current.Validate(out error))
					{
						return false;
					}
				}
			}
			foreach (TextureBlock textureBlock in this.TextureBlocks)
			{
				if (textureBlock.Type != TextureTypeEnum.Indexed_4bit && textureBlock.Type != TextureTypeEnum.Indexed_8bit)
				{
					error = string.Format("Not supported texture type 0x{0:X}", textureBlock.TypeBinary);
					return false;
				}
			}
			return true;
		}

		// Token: 0x06000040 RID: 64 RVA: 0x00003CE8 File Offset: 0x000028E8
		public Bitmap GetImage(TextureBlock textureBlock = null, PaletteBlock paletteBlock = null)
		{
			if (textureBlock == null)
			{
				textureBlock = this.TextureBlocks.FirstOrDefault<TextureBlock>();
			}
			if (paletteBlock == null)
			{
				paletteBlock = this.PaletteBlocks.FirstOrDefault<PaletteBlock>();
			}
			Bitmap bitmap = new Bitmap((int)textureBlock.Width, (int)textureBlock.Height, PixelFormat.Format32bppArgb);
			Dictionary<int, Color> dictionary = new Dictionary<int, Color>();
			for (int i = 0; i < paletteBlock.Colors.Count; i++)
			{
				dictionary.Add(i, paletteBlock.Colors[i]);
			}
			textureBlock.ApplyTextureData(bitmap, dictionary);
			return bitmap;
		}

		// Token: 0x06000041 RID: 65 RVA: 0x00003D64 File Offset: 0x00002964
		public void SetImage(Bitmap bitmap)
		{
			TextureBlock textureBlock = this.TextureBlocks.FirstOrDefault<TextureBlock>();
			PaletteBlock paletteBlock = this.PaletteBlocks.FirstOrDefault<PaletteBlock>();
			Bitmap bitmap2 = MedianCut.Quantize(bitmap, paletteBlock.Colors.Count);
			List<Color> allColors = MedianCut.GetAllColors(bitmap2);
			Dictionary<Color, int> dictionary = new Dictionary<Color, int>();
			foreach (Color key in allColors)
			{
				if (!dictionary.ContainsKey(key))
				{
					dictionary.Add(key, dictionary.Count);
				}
			}
			paletteBlock.Colors = dictionary.Keys.ToList<Color>();
			textureBlock.ApplyBitmapData(bitmap2, dictionary);
		}

		// Token: 0x06000042 RID: 66 RVA: 0x00003E14 File Offset: 0x00002A14
		public void Save(string fileName)
		{
			using (StreamHelper streamHelper = new StreamHelper(fileName, ByteEncoding.Little, FileMode.OpenOrCreate, FileAccess.ReadWrite, FileShare.Read))
			{
				streamHelper.Position = 16L;
				this.PaletteBlocks.FirstOrDefault<PaletteBlock>().Write(streamHelper);
				this.TextureBlocks.FirstOrDefault<TextureBlock>().Write(streamHelper);
			}
		}

		// Token: 0x04000016 RID: 22
		public Header Header;

		// Token: 0x04000017 RID: 23
		public List<PaletteBlock> PaletteBlocks;

		// Token: 0x04000018 RID: 24
		public List<TextureBlock> TextureBlocks;
	}
}
