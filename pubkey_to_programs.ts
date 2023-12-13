const func = async () => {
  const connection = new web3.Connection(
    "https://solana-mainnet.g.alchemy.com/v2/0XEUOjCO9i2kagRy0APOVHObWm8Gc6vz"
  );

  const accounts = await connection.getProgramAccounts(
    new web3.PublicKey("BPFLoaderUpgradeab1e11111111111111111111111"),
    {
      dataSlice: {
        offset: 4 + 8 + 1 + 32,
        length: 0,
      },
      filters: [
        {
          memcmp: {
            offset: 0,
            bytes: anchor.utils.bytes.bs58.encode([3, 0, 0, 0]),
          },
        },

        {
          memcmp: {
            offset: 4 + 8,
            bytes: anchor.utils.bytes.bs58.encode([1]),
          },
        },

        {
          memcmp: {
            offset: 4 + 8 + 1,
            bytes: new web3.PublicKey(
              "5xJypWhSThv1fJeDVPmyhxpANg4zTUrLuNNR8nhP1vpL"
            ).toBase58(),
          },
        },
      ],
    }
  );
  console.log("SEE RESULTS");
  console.log(accounts);
};

await func();
