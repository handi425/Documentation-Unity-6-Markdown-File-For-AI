[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AssetBundles-Cache.html)
  * [中文](/cn/current/Manual/AssetBundles-Cache.html)
  * [日本語](/ja/current/Manual/AssetBundles-Cache.html)
  * [한국어](/kr/current/Manual/AssetBundles-Cache.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AssetBundles-Cache.html)
  * [中文](/cn/current/Manual/AssetBundles-Cache.html)
  * [日本語](/ja/current/Manual/AssetBundles-Cache.html)
  * [한국어](/kr/current/Manual/AssetBundles-Cache.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [AssetBundles](AssetBundlesIntro.html)
  * AssetBundle compression and caching

[](AssetBundles-Native.html)

Using AssetBundles Natively

[](AssetBundles-Patching.html)

Patching with AssetBundles

# AssetBundle compression and caching

This page describes the **compression** A method of storing data that reduces
the amount of storage space it requires. See [Texture Compression](class-
TextureImporterOverride), [Animation Compression](class-
AnimationClip.html#AssetProperties), [Audio Compression](class-
AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) options supported in AssetBundles
and how this impacts the built-in AssetBundle caching support.

## AssetBundle compression formats

AssetBundle files are an archive format that comprises of a small header data
structure, followed by a content section containing its virtual files. The
header section is never compressed and the content section can optionally be
compressed. By default Unity compresses the content section with full-file
compression (LZMA) and caches AssetBundles with chunk-based compression (LZ4).

When `LZMA` compression is used the entire content section of the AssetBundle
file is compressed as a single stream. This full content approach results in
smaller file sizes than those with chunk-based compression. This is the
preferred format for AssetBundles downloaded from a Content Delivery Network
(CDN). The downside is that you must decompress the entire file into RAM in
order to read an Asset from these archives. This is best used when an
AssetBundle contains assets such that to use one asset from the bundle would
mean all assets are going to be loaded. Packaging all assets for a character
or **scene** A Scene contains the environments and menus of your game. Think
of each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) are some examples of bundles that might
use this. This is the format used when calling
`BuildPipeline.BuildAssetBundles` with no specific compression specified (e.g.
`BuildAssetBundleOptions.None`).

AssetBundles can also be built in such a way that the data is completely
uncompressed. The downside to being uncompressed is the larger file download
size because some types of content can be highly compressible inside a
AssetBundle. However, the load times once downloaded can be much faster
because no decompression needs to happen. This is particularly helpful when
only a few objects are loaded out of a larger AssetBundle. Uncompressed
AssetBundles are 16-byte aligned. This format is available by specifying the
flag `BuildAssetBundleOptions.UncompressedAssetBundle` when calling
BuildPipeline.BuildAssetBundles.

`LZ4` uses a chunk based algorithm which allows the AssetBundle to be
decompressed in pieces or “chunks”. While writing the AssetBundle each 128KB
chunk of the content is compressed prior to saving it. Because each chunk is
compressed individually the overall file size is larger than AssetBundles
compressed with LZMA. But this approach makes it possible to selectively
retrieve and load just the chunks needed for a requested object, rather than
decompressing the entire AssetBundle. LZ4 has comparable loading times to
uncompressed bundles with the added benefit of reduced size on disk. This is
the format preferred by the AssetBundle cache, which is described below, and
it can also be a good choice for AssetBundles that you distribute as part of
your installation or in other cases where size is not of paramount importance.
This format is available by specifying the flag
`BuildAssetBundleOptions.ChunkBasedCompression` when calling
BuildPipeline.BuildAssetBundles.

Because different data will compress with different degrees of size savings it
can make sense to experiment by rebuilding you project with each supported
option and measuring the actual size difference. The results can help guide a
decision about what format to use.

If you download and store data with a custom caching solution you can use
[AssetBundle.RecompressAssetBundleAsync](../ScriptReference/AssetBundle.RecompressAssetBundleAsync.html)
to change compression, for example to convert LZMA format AssetBundles to
uncompressed or LZ4 format after download.

**Note:** The Web platform doesn’t support LZMA compression for AssetBundles.
Use LZ4 compression with AssetBundles for the Web platform. For more
information, refer to [AssetBundles in Web](webgl-assetbundles.html).

## AssetBundle cache

When AssetBundles are being downloaded from a web service you need to consider
caching, so that a device does not have to download the same content each time
your player runs. Because AssetBundles may be rebuilt it is also important to
have a mechanism to replace a locally cached AssetBundle with a newer version.

Unity provides a built-in disk-based cache to store AssetBundles that are
downloaded through
[UnityWebRequestAssetBundle](../ScriptReference/Networking.UnityWebRequestAssetBundle.html).
To enable caching you must specify the version integer or version hash
parameter when calling `UnityWebRequestAssetBundle.GetAssetBundle`. By default
any AssetBundle added to the Disk Cache will be converted to LZ4 compression.
Hence it takes longer to initially download and load LZMA AssetBundles as the
recompression happens, but subsequent loads use the cached version and run
quickly. If [Caching.compressionEnabled](../ScriptReference/Caching-
compressionEnabled.html) is false, Unity writes AssetBundles into the Disk
Cache in uncompressed format.

When downloading AssetBundles over the internet it is important to take steps
to make sure that corrupted or tampered file content is not accepted into the
cache. You should specify the expected CRC when calling
`UnityWebRequestAssetBundle.GetAssetBundle` so that Unity can compare this
value against the downloaded content while it adds the file to the cache. The
CRC check can be performed at low cost during the conversion of LZMA
AssetBundles to LZ4. The CRC check does not need to be repeated again once the
validated file reaches the cache. See also [AssetBundle Download Integrity and
Security](AssetBundles-Integrity.html).

The [Caching](../ScriptReference/Caching.html) class can be used to manage the
built-in AssetBundle cache, for example to clear its content or to check if an
AssetBundle is already cached.

## AssetBundle Memory Usage

For performance purposes Unity holds some uncompressed data in memory while a
chunk-based or uncompressed AssetBundle is loaded. But this caching has fixed
size regardless of how large the underlying AssetBundle file is.

To load an AssetBundle, Unity requires random access to its content, either
through a file on disk, a file in Memory or a C# FileStream. It also requires
that the AssetBundle is uncompressed or uses chunk-based compression (LZ4). In
order to establish a loadable AssetBundle, Unity will sometimes need to create
a temporary in-memory AssetBundle. This is not always a bad thing, as
AssetBundle content can load quickly once it is in memory. But in many cases
it is better to try to have the file represented on disk, as a local
AssetBundle or cached download, so that RAM usage is minimized and on-the-fly
compression conversion does not slow down load times.

Temporary in-memory AssetBundles will be created in the following cases:

  * Calling [AssetBundle.LoadFromFile](../ScriptReference/AssetBundle.LoadFromFile.html) and [AssetBundle.LoadFromFileAsync](../ScriptReference/AssetBundle.LoadFromFileAsync.html) when the input AssetBundle uses LZMA compression
  * All calls to [AssetBundle.LoadFromMemory](../ScriptReference/AssetBundle.LoadFromMemory.html) and [AssetBundle.LoadFromMemoryAsync](../ScriptReference/AssetBundle.LoadFromMemoryAsync.html).
  * Calling [AssetBundle.LoadFromStream](../ScriptReference/AssetBundle.LoadFromStream.html) and [AssetBundle.LoadFromStreamAsync](../ScriptReference/AssetBundle.LoadFromStreamAsync.html) when the input AssetBundle uses LZMA compression.
  * Calling [UnityWebRequestAssetBundle.GetAssetBundle](../ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html) without providing a version integer or hash, or on the Web platform which doesn’t support disk-based AssetBundle Caching.

The memory used by the temporary file is released when all reads have
completed and AssetBundle.Unload is called.

Note: On platforms that support disk-based AssetBundle caching, the
[Caching.compressionEnabled](../ScriptReference/Caching-
compressionEnabled.html) setting will influence the format that is used for
temporary in-memory AssetBundles. By default it is true and in-memory
AssetBundles use LZ4. When Caching.compressionEnabled is false these in-memory
files will be uncompressed and hence potentially take substantially more RAM.
On platforms that do not support caching the in-memory format is always LZ4.
If the input is a different format then an on-the-fly conversion is performed,
which can add to load times.

Note: doing a CRC check when calling AssetBundle.LoadFromFile,
AssetBundle.LoadFromFileAsync, AssetBundle.LoadFromStream or
AssetBundle.LoadFromStreamAsync for a chunk-based file will force a full read
and decompression of each chunk of the file. This calculation happens chunk by
chunk, rather than loading the full file into RAM, so it is not a memory
concern, but it can slow down load times. For a LZMA format AssetBundle there
is no significant extra cost to perform the CRC check, because loading it
always does a read and decompression of all the content.

Memory **profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) tools, such as the [Memory
Profiler](https://docs.unity3d.com/Packages/com.unity.memoryprofiler@latest)
package, can be useful to check how much memory your loaded AssetBundles are
using.

[](AssetBundles-Native.html)

Using AssetBundles Natively

[](AssetBundles-Patching.html)

Patching with AssetBundles

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

