using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Runtime.InteropServices;

namespace TalesOfDestinyTm2Converter.Quantizer
{
	// Token: 0x02000009 RID: 9
	public static class MedianCut
	{
		// Token: 0x06000049 RID: 73 RVA: 0x00004280 File Offset: 0x00002E80
		public static Bitmap Quantize(Bitmap bitmap, int colorsCount)
		{
			List<Color> list = (from g in MedianCut.GetAllColors(bitmap).ToLookup((Color g) => g)
			select g.Key).ToList<Color>();
			if (list.Count < colorsCount)
			{
				colorsCount = list.Count;
			}
			List<Bucket> list2 = new List<Bucket>
			{
				new Bucket(list)
			};
			while (list2.Count < colorsCount)
			{
				List<Bucket> list3 = new List<Bucket>();
				for (int i = 0; i < list2.Count; i++)
				{
					if (list3.Count + (list2.Count - i) >= colorsCount)
					{
						list3.AddRange(list2.GetRange(i, list2.Count - i));
						break;
					}
					Tuple<Bucket, Bucket> tuple = list2[i].Split();
					if (tuple.Item1.colours.Count > 0)
					{
						list3.Add(tuple.Item1);
					}
					if (tuple.Item2.colours.Count > 0)
					{
						list3.Add(tuple.Item2);
					}
				}
				list2 = list3;
			}
			Dictionary<Color, Color> dictionary = new Dictionary<Color, Color>();
			foreach (Bucket bucket in list2)
			{
				foreach (KeyValuePair<Color, int> keyValuePair in bucket.colours)
				{
					dictionary.Add(keyValuePair.Key, bucket.Colour);
				}
			}
			Bitmap bitmap2 = new Bitmap(bitmap.Width, bitmap.Height);
			for (int j = 0; j < bitmap.Width; j++)
			{
				for (int k = 0; k < bitmap.Height; k++)
				{
					Color color = dictionary[bitmap.GetPixel(j, k)];
					bitmap2.SetPixel(j, k, color);
				}
			}
			return bitmap2;
		}

		// Token: 0x0600004A RID: 74 RVA: 0x000044AC File Offset: 0x000030AC
		public static List<Color> GetAllColors(Bitmap bitmap)
		{
			List<Color> list = new List<Color>();
			BitmapData bitmapData = bitmap.LockBits(new Rectangle(0, 0, bitmap.Width, bitmap.Height), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
			for (int i = 0; i < bitmap.Height; i++)
			{
				for (int j = 0; j < bitmap.Width; j++)
				{
					int argb = Marshal.ReadInt32(bitmapData.Scan0, j * 4 + i * bitmapData.Stride);
					list.Add(Color.FromArgb(argb));
				}
			}
			bitmap.UnlockBits(bitmapData);
			return list;
		}
	}
}
