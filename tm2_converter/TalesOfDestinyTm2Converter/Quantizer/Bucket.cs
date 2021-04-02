using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;

namespace TalesOfDestinyTm2Converter.Quantizer
{
	// Token: 0x02000008 RID: 8
	public class Bucket
	{
		// Token: 0x17000014 RID: 20
		// (get) Token: 0x06000044 RID: 68 RVA: 0x00003E74 File Offset: 0x00002A74
		public Color Colour { get; }

		// Token: 0x06000045 RID: 69 RVA: 0x00003E7C File Offset: 0x00002A7C
		public Bucket(IEnumerable<Color> colours)
		{
			this.colours = colours.ToLookup((Color c) => c).ToDictionary((IGrouping<Color, Color> c) => c.Key, (IGrouping<Color, Color> c) => c.Count<Color>());
			this.Colour = Bucket.Average(this.colours);
		}

		// Token: 0x06000046 RID: 70 RVA: 0x00003F10 File Offset: 0x00002B10
		public Bucket(IEnumerable<KeyValuePair<Color, int>> enumerable)
		{
			this.colours = enumerable.ToDictionary((KeyValuePair<Color, int> c) => c.Key, (KeyValuePair<Color, int> c) => c.Value);
			this.Colour = Bucket.Average(this.colours);
		}

		// Token: 0x06000047 RID: 71 RVA: 0x00003F80 File Offset: 0x00002B80
		private static Color Average(IEnumerable<KeyValuePair<Color, int>> colours)
		{
			int num = colours.Sum((KeyValuePair<Color, int> c) => c.Value);
			if (num == 0)
			{
				return Color.Black;
			}
			return Color.FromArgb(colours.Sum((KeyValuePair<Color, int> c) => (int)c.Key.A * c.Value) / num, colours.Sum((KeyValuePair<Color, int> c) => (int)c.Key.R * c.Value) / num, colours.Sum((KeyValuePair<Color, int> c) => (int)c.Key.G * c.Value) / num, colours.Sum((KeyValuePair<Color, int> c) => (int)c.Key.B * c.Value) / num);
		}

		// Token: 0x06000048 RID: 72 RVA: 0x00004060 File Offset: 0x00002C60
		public Tuple<Bucket, Bucket> Split()
		{
			int num = (int)(this.colours.Keys.Max((Color c) => c.R) - this.colours.Keys.Min((Color c) => c.R));
			int num2 = (int)(this.colours.Keys.Max((Color c) => c.G) - this.colours.Keys.Min((Color c) => c.G));
			int num3 = (int)(this.colours.Keys.Max((Color c) => c.B) - this.colours.Keys.Min((Color c) => c.B));
			Func<Color, int> sorter;
			if (num > num2)
			{
				if (num > num3)
				{
					sorter = ((Color c) => (int)c.R);
				}
				else
				{
					sorter = ((Color c) => (int)c.B);
				}
			}
			else if (num2 > num3)
			{
				sorter = ((Color c) => (int)c.G);
			}
			else
			{
				sorter = ((Color c) => (int)c.B);
			}
			IOrderedEnumerable<KeyValuePair<Color, int>> source = from c in this.colours
			orderby sorter(c.Key)
			select c;
			int count = source.Count<KeyValuePair<Color, int>>() / 2;
			Bucket item = new Bucket(source.Take(count));
			Bucket item2 = new Bucket(source.Skip(count));
			return new Tuple<Bucket, Bucket>(item, item2);
		}

		// Token: 0x04000019 RID: 25
		public readonly IDictionary<Color, int> colours;
	}
}
