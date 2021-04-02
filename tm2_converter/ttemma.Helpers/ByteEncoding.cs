using System;
using System.ComponentModel;
using System.Diagnostics;

namespace ttemma.Helpers
{
	// Token: 0x02000002 RID: 2
	public enum ByteEncoding
	{
		// Token: 0x04000002 RID: 2
		[Description("Not set byte encoding")]
		None,
		// Token: 0x04000003 RID: 3
		[Description("Read bytes from right to left.")]
		Little,
		// Token: 0x04000004 RID: 4
		[Description("Read bytes from left to right.")]
		Big
	}
}
