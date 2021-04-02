using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.IO;

namespace TalesOfDestinyTm2Converter
{
	// Token: 0x02000004 RID: 4
	internal class Program
	{
		// Token: 0x06000025 RID: 37 RVA: 0x00003668 File Offset: 0x00002268
		private static void Main(string[] args)
		{
			if (args.Length == 0)
			{
				return;
			}
			if (args[0] == "-e")
			{
				TM2 tm = TM2.ReadBinary(args[1]);
				string filename = args[1] + ".png";
				string value;
				if (!tm.Validate(out value))
				{
					Console.WriteLine(value);
					filename = args[1] + ".ERROR.png";
				}
				tm.GetImage(null, null).Save(filename, ImageFormat.Png);
			}
			if (args[0] == "-r")
			{
				TM2 tm2 = TM2.ReadBinary(args[1]);
				string str;
				if (!tm2.Validate(out str))
				{
					Console.WriteLine("Repack error: " + str);
					return;
				}
				if (!File.Exists(args[1] + ".png"))
				{
					Console.WriteLine("Repack error: file " + args[1] + ".png not found");
					return;
				}
				Bitmap image = (Bitmap)Image.FromFile(args[1] + ".png");
				tm2.SetImage(image);
				tm2.Save(args[1]);
			}
		}
	}
}
