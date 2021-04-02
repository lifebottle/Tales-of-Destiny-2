using System;
using ttemma.Helpers;

namespace TalesOfDestinyTm2Converter
{
	// Token: 0x02000002 RID: 2
	public class Header
	{
		// Token: 0x17000001 RID: 1
		// (get) Token: 0x06000001 RID: 1 RVA: 0x000030D4 File Offset: 0x00001CD4
		// (set) Token: 0x06000002 RID: 2 RVA: 0x000030DC File Offset: 0x00001CDC
		public byte CountTextures { get; set; }

		// Token: 0x17000002 RID: 2
		// (get) Token: 0x06000003 RID: 3 RVA: 0x000030E5 File Offset: 0x00001CE5
		// (set) Token: 0x06000004 RID: 4 RVA: 0x000030ED File Offset: 0x00001CED
		public byte CountPalette { get; set; }

		// Token: 0x17000003 RID: 3
		// (get) Token: 0x06000005 RID: 5 RVA: 0x000030F6 File Offset: 0x00001CF6
		// (set) Token: 0x06000006 RID: 6 RVA: 0x000030FE File Offset: 0x00001CFE
		public byte CountUnknown { get; set; }

		// Token: 0x17000004 RID: 4
		// (get) Token: 0x06000007 RID: 7 RVA: 0x00003107 File Offset: 0x00001D07
		// (set) Token: 0x06000008 RID: 8 RVA: 0x0000310F File Offset: 0x00001D0F
		public byte Dummy { get; set; }

		// Token: 0x17000005 RID: 5
		// (get) Token: 0x06000009 RID: 9 RVA: 0x00003118 File Offset: 0x00001D18
		// (set) Token: 0x0600000A RID: 10 RVA: 0x00003120 File Offset: 0x00001D20
		public int Dummy2 { get; set; }

		// Token: 0x17000006 RID: 6
		// (get) Token: 0x0600000B RID: 11 RVA: 0x00003129 File Offset: 0x00001D29
		// (set) Token: 0x0600000C RID: 12 RVA: 0x00003131 File Offset: 0x00001D31
		public int Dummy3 { get; set; }

		// Token: 0x0600000D RID: 13 RVA: 0x0000313C File Offset: 0x00001D3C
		public static Header Read(StreamHelper streamHelper)
		{
			Header header = new Header();
			uint num = streamHelper.ReadUInt32(ByteEncoding.Big);
			if (num != 1414345280U)
			{
				throw new NotSupportedException(string.Format("Invalid magic 0x{0:X}", num));
			}
			header.CountTextures = streamHelper.ReadByte();
			header.CountPalette = streamHelper.ReadByte();
			header.CountUnknown = streamHelper.ReadByte();
			header.Dummy = streamHelper.ReadByte();
			header.Dummy2 = streamHelper.ReadInt32(ByteEncoding.None);
			header.Dummy3 = streamHelper.ReadInt32(ByteEncoding.None);
			return header;
		}
	}
}
