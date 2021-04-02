using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using ttemma.Helpers;

namespace TalesOfDestinyTm2Converter
{
	// Token: 0x02000003 RID: 3
	public class PaletteBlock
	{
		// Token: 0x17000007 RID: 7
		// (get) Token: 0x0600000F RID: 15 RVA: 0x000031C6 File Offset: 0x00001DC6
		// (set) Token: 0x06000010 RID: 16 RVA: 0x000031CE File Offset: 0x00001DCE
		public int Length { get; set; }

		// Token: 0x17000008 RID: 8
		// (get) Token: 0x06000011 RID: 17 RVA: 0x000031D7 File Offset: 0x00001DD7
		// (set) Token: 0x06000012 RID: 18 RVA: 0x000031DF File Offset: 0x00001DDF
		public int Dummy { get; set; }

		// Token: 0x17000009 RID: 9
		// (get) Token: 0x06000013 RID: 19 RVA: 0x000031E8 File Offset: 0x00001DE8
		// (set) Token: 0x06000014 RID: 20 RVA: 0x000031F0 File Offset: 0x00001DF0
		public int Dummy2 { get; set; }

		// Token: 0x1700000A RID: 10
		// (get) Token: 0x06000015 RID: 21 RVA: 0x000031F9 File Offset: 0x00001DF9
		// (set) Token: 0x06000016 RID: 22 RVA: 0x00003201 File Offset: 0x00001E01
		public short Width { get; set; }

		// Token: 0x1700000B RID: 11
		// (get) Token: 0x06000017 RID: 23 RVA: 0x0000320A File Offset: 0x00001E0A
		// (set) Token: 0x06000018 RID: 24 RVA: 0x00003212 File Offset: 0x00001E12
		public short Height { get; set; }

		// Token: 0x1700000C RID: 12
		// (get) Token: 0x06000019 RID: 25 RVA: 0x0000321B File Offset: 0x00001E1B
		// (set) Token: 0x0600001A RID: 26 RVA: 0x00003223 File Offset: 0x00001E23
		public List<Color> Colors { get; set; }

		// Token: 0x0600001B RID: 27 RVA: 0x0000322C File Offset: 0x00001E2C
		private static Color ReadColor(StreamHelper streamHelper)
		{
			uint num = streamHelper.ReadUInt32(ByteEncoding.Big);
			byte red = (byte)(num >> 24 & 255U);
			byte green = (byte)(num >> 16 & 255U);
			byte blue = (byte)(num >> 8 & 255U);
			return Color.FromArgb((int)((byte)Math.Min((num & 255U) << 1, 255U)), (int)red, (int)green, (int)blue);
		}

		// Token: 0x0600001C RID: 28 RVA: 0x0000327E File Offset: 0x00001E7E
		private static void WriteColor(StreamHelper streamHelper, Color color)
		{
			streamHelper.WriteByte(color.R);
			streamHelper.WriteByte(color.G);
			streamHelper.WriteByte(color.B);
			streamHelper.WriteByte((byte)(color.A & 128));
		}

		// Token: 0x0600001D RID: 29 RVA: 0x000032BC File Offset: 0x00001EBC
		private static List<Color> ReadColorBlock(StreamHelper streamHelper)
		{
			List<Color> list = new List<Color>(8);
			for (int i = 0; i < 8; i++)
			{
				list.Add(PaletteBlock.ReadColor(streamHelper));
			}
			return list;
		}

		// Token: 0x0600001E RID: 30 RVA: 0x000032E9 File Offset: 0x00001EE9
		private List<Color> GetColorBlock(int idx)
		{
			return this.Colors.Skip(idx * 8).Take(8).ToList<Color>();
		}

		// Token: 0x0600001F RID: 31 RVA: 0x00003304 File Offset: 0x00001F04
		private void WriteColorList(StreamHelper streamHelper, List<Color> colorList)
		{
			foreach (Color color in colorList)
			{
				PaletteBlock.WriteColor(streamHelper, color);
			}
		}

		// Token: 0x06000020 RID: 32 RVA: 0x00003354 File Offset: 0x00001F54
		public static PaletteBlock Read(StreamHelper streamHelper)
		{
			PaletteBlock paletteBlock = new PaletteBlock();
			paletteBlock.Length = streamHelper.ReadInt32(ByteEncoding.None);
			paletteBlock.Dummy = streamHelper.ReadInt32(ByteEncoding.None);
			paletteBlock.Dummy2 = streamHelper.ReadInt32(ByteEncoding.None);
			paletteBlock.Width = streamHelper.ReadInt16(ByteEncoding.None);
			paletteBlock.Height = streamHelper.ReadInt16(ByteEncoding.None);
			paletteBlock.Colors = new List<Color>();
			int num = (paletteBlock.Length - 16) / 4;
			if (num <= 16)
			{
				for (int i = 0; i < num; i++)
				{
					paletteBlock.Colors.Add(PaletteBlock.ReadColor(streamHelper));
				}
			}
			else
			{
				for (int j = 0; j < num / 8 / 4; j++)
				{
					List<Color> collection = PaletteBlock.ReadColorBlock(streamHelper);
					List<Color> collection2 = PaletteBlock.ReadColorBlock(streamHelper);
					List<Color> collection3 = PaletteBlock.ReadColorBlock(streamHelper);
					List<Color> collection4 = PaletteBlock.ReadColorBlock(streamHelper);
					paletteBlock.Colors.AddRange(collection);
					paletteBlock.Colors.AddRange(collection3);
					paletteBlock.Colors.AddRange(collection2);
					paletteBlock.Colors.AddRange(collection4);
				}
			}
			return paletteBlock;
		}

		// Token: 0x06000021 RID: 33 RVA: 0x00003448 File Offset: 0x00002048
		public void Write(StreamHelper streamHelper)
		{
			streamHelper.Write<int>(this.Length, ByteEncoding.None);
			streamHelper.Write<int>(this.Dummy, ByteEncoding.None);
			streamHelper.Write<int>(this.Dummy, ByteEncoding.None);
			streamHelper.Write<short>(this.Width, ByteEncoding.None);
			streamHelper.Write<short>(this.Height, ByteEncoding.None);
			this.PrepareColors();
			int num = (this.Length - 16) / 4;
			if (num <= 16)
			{
				for (int i = 0; i < this.Colors.Count; i++)
				{
					PaletteBlock.WriteColor(streamHelper, this.Colors[i]);
				}
				return;
			}
			int num2 = 0;
			for (int j = 0; j < num / 8 / 4; j++)
			{
				List<Color> colorBlock = this.GetColorBlock(num2++);
				List<Color> colorBlock2 = this.GetColorBlock(num2++);
				List<Color> colorBlock3 = this.GetColorBlock(num2++);
				List<Color> colorBlock4 = this.GetColorBlock(num2++);
				this.WriteColorList(streamHelper, colorBlock);
				this.WriteColorList(streamHelper, colorBlock3);
				this.WriteColorList(streamHelper, colorBlock2);
				this.WriteColorList(streamHelper, colorBlock4);
			}
		}

		// Token: 0x06000022 RID: 34 RVA: 0x00003540 File Offset: 0x00002140
		private void PrepareColors()
		{
			if ((this.Length - 16) / 4 <= 16)
			{
				if (this.Colors.Count < 16)
				{
					while (this.Colors.Count < 16)
					{
						this.Colors.Add(Color.Black);
					}
				}
				if (this.Colors.Count > 16)
				{
					this.Colors = this.Colors.Take(16).ToList<Color>();
					return;
				}
			}
			else
			{
				if (this.Colors.Count < 256)
				{
					while (this.Colors.Count < 256)
					{
						this.Colors.Add(Color.Black);
					}
				}
				if (this.Colors.Count > 256)
				{
					this.Colors = this.Colors.Take(256).ToList<Color>();
				}
			}
		}

		// Token: 0x06000023 RID: 35 RVA: 0x00003618 File Offset: 0x00002218
		public bool Validate(out string error)
		{
			error = string.Empty;
			if (this.Width != 8 && this.Width != 16)
			{
				error = "Not supported palette format";
				return false;
			}
			if (this.Height != 2 && this.Height != 16)
			{
				error = "Not supported palette format";
				return false;
			}
			return true;
		}
	}
}
