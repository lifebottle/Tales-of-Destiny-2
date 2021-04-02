using System;
using System.Security.Cryptography;

namespace ttemma.Helpers.Cryptography
{
	// Token: 0x02000005 RID: 5
	public class CRC32CryptoProvider : HashAlgorithm
	{
		// Token: 0x06000043 RID: 67 RVA: 0x00003794 File Offset: 0x00001D94
		private void InitializeTable()
		{
			this._cryptoTable = new uint[256];
			for (int i = 0; i < 256; i++)
			{
				uint num = (uint)((uint)i << 24);
				for (int j = 0; j < 8; j++)
				{
					if ((num & 2147483648U) != 0U)
					{
						num = (num << 1 ^ this._currentPolynominal);
					}
					else
					{
						num <<= 1;
					}
				}
				this._cryptoTable[i] = num;
			}
		}

		// Token: 0x06000044 RID: 68 RVA: 0x000037F5 File Offset: 0x00001DF5
		public override void Initialize()
		{
			this._hash = this._currentSeed;
		}

		// Token: 0x06000045 RID: 69 RVA: 0x00003804 File Offset: 0x00001E04
		public CRC32CryptoProvider(uint polynomial = 79764919U, uint seed = 4294967295U, uint xorValue = 4294967295U, bool refIn = true, bool refOut = true)
		{
			this._currentPolynominal = polynomial;
			this._hash = seed;
			this._currentSeed = seed;
			this._currentXor = xorValue;
			this._currentRefIn = refIn;
			this._currentRefOut = refOut;
			this.InitializeTable();
		}

		// Token: 0x06000046 RID: 70 RVA: 0x0000384B File Offset: 0x00001E4B
		public CRC32CryptoProvider() : this(79764919U, uint.MaxValue, uint.MaxValue, true, true)
		{
		}

		// Token: 0x06000047 RID: 71 RVA: 0x0000385C File Offset: 0x00001E5C
		protected override void HashCore(byte[] array, int ibStart, int cbSize)
		{
			this._hash = CRC32CryptoProvider.Calculate(this._cryptoTable, this._currentSeed, this._currentXor, this._currentRefIn, this._currentRefOut, array, ibStart, cbSize);
		}

		// Token: 0x06000048 RID: 72 RVA: 0x00003895 File Offset: 0x00001E95
		protected override byte[] HashFinal()
		{
			return BitConverter.GetBytes(this._hash);
		}

		// Token: 0x06000049 RID: 73 RVA: 0x000038A4 File Offset: 0x00001EA4
		private static byte Reflect8(byte val)
		{
			byte b = 0;
			for (int i = 0; i < 8; i++)
			{
				if (((int)val & 1 << i) != 0)
				{
					b |= (byte)(1 << 7 - i);
				}
			}
			return b;
		}

		// Token: 0x0600004A RID: 74 RVA: 0x000038D8 File Offset: 0x00001ED8
		private static uint Reflect32(uint val)
		{
			uint num = 0U;
			for (int i = 0; i < 32; i++)
			{
				if (((ulong)val & (ulong)(1L << (i & 31))) != 0UL)
				{
					num |= 1U << 31 - i;
				}
			}
			return num;
		}

		// Token: 0x0600004B RID: 75 RVA: 0x00003910 File Offset: 0x00001F10
		private static uint Calculate(uint[] table, uint seed, uint xorValue, bool refIn, bool refOut, byte[] array, int offset, int count)
		{
			uint num = seed;
			for (int i = offset; i < offset + count; i++)
			{
				byte b = refIn ? CRC32CryptoProvider.Reflect8(array[i]) : array[i];
				num = (uint)((ulong)num ^ (ulong)((long)((long)b << 24)));
				byte b2 = (byte)(num >> 24);
				num = (num << 8 ^ table[(int)b2]);
			}
			if (refOut)
			{
				num = CRC32CryptoProvider.Reflect32(num);
			}
			return num ^ xorValue;
		}

		// Token: 0x04000008 RID: 8
		private const uint DefaultPolynomial = 79764919U;

		// Token: 0x04000009 RID: 9
		private const uint DefaultSeed = 4294967295U;

		// Token: 0x0400000A RID: 10
		private const uint DefaultXor = 4294967295U;

		// Token: 0x0400000B RID: 11
		private uint[] _cryptoTable;

		// Token: 0x0400000C RID: 12
		private uint _currentSeed;

		// Token: 0x0400000D RID: 13
		private uint _currentPolynominal;

		// Token: 0x0400000E RID: 14
		private uint _currentXor;

		// Token: 0x0400000F RID: 15
		private bool _currentRefIn;

		// Token: 0x04000010 RID: 16
		private bool _currentRefOut;

		// Token: 0x04000011 RID: 17
		private uint _hash;
	}
}
