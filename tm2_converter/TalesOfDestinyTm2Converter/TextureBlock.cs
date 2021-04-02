using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using ttemma.Helpers;

namespace TalesOfDestinyTm2Converter
{
	// Token: 0x02000005 RID: 5
	public class TextureBlock
	{
		// Token: 0x1700000D RID: 13
		// (get) Token: 0x06000027 RID: 39 RVA: 0x00003758 File Offset: 0x00002358
		// (set) Token: 0x06000028 RID: 40 RVA: 0x00003760 File Offset: 0x00002360
		public int Length { get; set; }

		// Token: 0x1700000E RID: 14
		// (get) Token: 0x06000029 RID: 41 RVA: 0x00003769 File Offset: 0x00002369
		// (set) Token: 0x0600002A RID: 42 RVA: 0x00003771 File Offset: 0x00002371
		public int TypeBinary { get; set; }

		// Token: 0x1700000F RID: 15
		// (get) Token: 0x0600002B RID: 43 RVA: 0x0000377A File Offset: 0x0000237A
		public TextureTypeEnum Type
		{
			get
			{
				return (TextureTypeEnum)this.TypeBinary;
			}
		}

		// Token: 0x17000010 RID: 16
		// (get) Token: 0x0600002C RID: 44 RVA: 0x00003782 File Offset: 0x00002382
		// (set) Token: 0x0600002D RID: 45 RVA: 0x0000378A File Offset: 0x0000238A
		public int Dummy { get; set; }

		// Token: 0x17000011 RID: 17
		// (get) Token: 0x0600002E RID: 46 RVA: 0x00003793 File Offset: 0x00002393
		// (set) Token: 0x0600002F RID: 47 RVA: 0x0000379B File Offset: 0x0000239B
		public short Width { get; set; }

		// Token: 0x17000012 RID: 18
		// (get) Token: 0x06000030 RID: 48 RVA: 0x000037A4 File Offset: 0x000023A4
		// (set) Token: 0x06000031 RID: 49 RVA: 0x000037AC File Offset: 0x000023AC
		public short Height { get; set; }

		// Token: 0x17000013 RID: 19
		// (get) Token: 0x06000032 RID: 50 RVA: 0x000037B5 File Offset: 0x000023B5
		// (set) Token: 0x06000033 RID: 51 RVA: 0x000037BD File Offset: 0x000023BD
		public byte[] Data { get; set; }

		// Token: 0x06000034 RID: 52 RVA: 0x000037C8 File Offset: 0x000023C8
		public static TextureBlock Read(StreamHelper streamHelper)
		{
			TextureBlock textureBlock = new TextureBlock();
			textureBlock.Length = streamHelper.ReadInt32(ByteEncoding.None);
			textureBlock.TypeBinary = streamHelper.ReadInt32(ByteEncoding.None);
			textureBlock.Dummy = streamHelper.ReadInt32(ByteEncoding.None);
			textureBlock.Width = streamHelper.ReadInt16(ByteEncoding.None);
			textureBlock.Height = streamHelper.ReadInt16(ByteEncoding.None);
			textureBlock.Data = streamHelper.ReadByteArray(textureBlock.Length - 16);
			return textureBlock;
		}

		// Token: 0x06000035 RID: 53 RVA: 0x00003834 File Offset: 0x00002434
		public void Write(StreamHelper streamHelper)
		{
			streamHelper.Write<int>(this.Length, ByteEncoding.None);
			streamHelper.Write<int>(this.TypeBinary, ByteEncoding.None);
			streamHelper.Write<int>(this.Dummy, ByteEncoding.None);
			streamHelper.Write<short>(this.Width, ByteEncoding.None);
			streamHelper.Write<short>(this.Height, ByteEncoding.None);
			streamHelper.WriteByteArray(this.Data);
		}

		// Token: 0x06000036 RID: 54 RVA: 0x00003890 File Offset: 0x00002490
		public PixelFormat GetPixelFormat()
		{
			TextureTypeEnum type = this.Type;
			if (type == TextureTypeEnum.Indexed_8bit)
			{
				return PixelFormat.Format8bppIndexed;
			}
			if (type == TextureTypeEnum.Indexed_4bit)
			{
				return PixelFormat.Format4bppIndexed;
			}
			throw new NotSupportedException(string.Format("Not supported texture type 0x{0:X}", this.TypeBinary));
		}

		// Token: 0x06000037 RID: 55 RVA: 0x000038D4 File Offset: 0x000024D4
		public void ApplyTextureData(Bitmap bitmap, Dictionary<int, Color> palette)
		{
			TextureTypeEnum type = this.Type;
			if (type == TextureTypeEnum.Indexed_8bit)
			{
				this.Apply8bit(bitmap, palette);
				return;
			}
			if (type == TextureTypeEnum.Indexed_4bit)
			{
				this.Apply4bit(bitmap, palette);
				return;
			}
			throw new NotSupportedException(string.Format("Not supported texture type 0x{0:X}", this.TypeBinary));
		}

		// Token: 0x06000038 RID: 56 RVA: 0x00003920 File Offset: 0x00002520
		private void Apply4bit(Bitmap bitmap, Dictionary<int, Color> palette)
		{
			int num = 0;
			for (int i = 0; i < (int)this.Height; i++)
			{
				for (int j = 0; j < (int)this.Width; j += 2)
				{
					byte b = this.Data[num++];
					byte key = (byte)(b >> 4 & 15);
					byte key2 = (Byte)(b & 15);
					bitmap.SetPixel(j, i, palette[(int)key2]);
					bitmap.SetPixel(j + 1, i, palette[(int)key]);
				}
			}
		}

		// Token: 0x06000039 RID: 57 RVA: 0x0000398C File Offset: 0x0000258C
		private void Apply8bit(Bitmap bitmap, Dictionary<int, Color> palette)
		{
			int num = 0;
			for (int i = 0; i < (int)this.Height; i++)
			{
				for (int j = 0; j < (int)this.Width; j++)
				{
					byte key = this.Data[num++];
					bitmap.SetPixel(j, i, palette[(int)key]);
				}
			}
		}

		// Token: 0x0600003A RID: 58 RVA: 0x000039DC File Offset: 0x000025DC
		public void ApplyBitmapData(Bitmap bitmap, Dictionary<Color, int> indexByColor)
		{
			TextureTypeEnum type = this.Type;
			if (type == TextureTypeEnum.Indexed_8bit)
			{
				this.ApplyBitmap8bit(bitmap, indexByColor);
				return;
			}
			if (type == TextureTypeEnum.Indexed_4bit)
			{
				this.ApplyBitmap4bit(bitmap, indexByColor);
				return;
			}
			throw new NotSupportedException(string.Format("Not supported texture type 0x{0:X}", this.TypeBinary));
		}

		// Token: 0x0600003B RID: 59 RVA: 0x00003A28 File Offset: 0x00002628
		public void ApplyBitmap4bit(Bitmap bitmap, Dictionary<Color, int> indexByColor)
		{
			List<byte> list = new List<byte>();
			for (int i = 0; i < (int)this.Height; i++)
			{
				for (int j = 0; j < (int)this.Width; j += 2)
				{
					Color pixel = bitmap.GetPixel(j, i);
					Color pixel2 = bitmap.GetPixel(j + 1, i);
					int num;
					if (!indexByColor.TryGetValue(pixel, out num))
					{
						throw new Exception("Convert error.");
					}
					int num2;
					if (!indexByColor.TryGetValue(pixel2, out num2))
					{
						throw new Exception("Convert error.");
					}
					int num3 = num2 << 4 | num;
					list.Add((byte)num3);
				}
			}
			this.Data = list.ToArray();
		}

		// Token: 0x0600003C RID: 60 RVA: 0x00003AC0 File Offset: 0x000026C0
		public void ApplyBitmap8bit(Bitmap bitmap, Dictionary<Color, int> indexByColor)
		{
			List<byte> list = new List<byte>();
			for (int i = 0; i < (int)this.Height; i++)
			{
				for (int j = 0; j < (int)this.Width; j++)
				{
					Color pixel = bitmap.GetPixel(j, i);
					int num;
					if (!indexByColor.TryGetValue(pixel, out num))
					{
						throw new Exception("Convert error.");
					}
					list.Add((byte)num);
				}
			}
			this.Data = list.ToArray();
		}
	}
}
