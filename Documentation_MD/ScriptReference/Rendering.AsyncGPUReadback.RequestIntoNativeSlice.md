[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [AsyncGPUReadback](Rendering.AsyncGPUReadback.html).RequestIntoNativeSlice

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output, [Texture](Texture.html) src,
int mipIndex, Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output, [Texture](Texture.html) src,
int mipIndex, [TextureFormat](TextureFormat.html) dstFormat,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output, [Texture](Texture.html) src,
int mipIndex,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
dstFormat, Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output, [Texture](Texture.html) src,
int mipIndex, int x, int width, int y, int height, int z, int depth,
[TextureFormat](TextureFormat.html) dstFormat, Action<AsyncGPUReadbackRequest>
callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output, [Texture](Texture.html) src,
int mipIndex, int x, int width, int y, int height, int z, int depth,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
dstFormat, Action<AsyncGPUReadbackRequest> callback);

### Parameters

output | Reference to the NativeSlice to write the data into. The underlying memory cannot be Disposed until the request is complete.  
---|---  
src | The [Texture](Texture.html) resource to read the data from.  
mipIndex | The index of the mipmap to fetch.  
dstFormat | The target [TextureFormat](TextureFormat.html) of the data. Conversion happens automatically if this format is different from the format stored on the GPU.  
x | The starting x-coordinate, in pixels, of the Texture data to fetch.  
width | The width, in pixels, of the Texture data to fetch.  
y | The starting y-coordinate, in pixels, of the Texture data to fetch.  
height | The height, in pixels, of the Texture data to fetch.  
z | The starting z-coordinate, in pixels, of the [Texture3D](Texture3D.html) to fetch. For TextureCube, [Texture2DArray](Texture2DArray.html), and TextureCubeArray, this is the index of the start layer.  
depth | The depth, in pixels of the [Texture3D](Texture3D.html) to fetch. For TextureCube, [Texture2DArray](Texture2DArray.html), and TextureCubeArray, this is the number of layers to retrieve.  
callback | An optional delegate System.Action to call after Unity completes the request. When Unity calls the delegate, it passes the completed request as a parameter to the System.Action.  
  
### Returns

**AsyncGPUReadbackRequest** Returns an
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html) that you can
use to determine when the data is available. Otherwise, returns a request with
an error.

### Description

Retrieves data asynchronously from a GPU Texture resource.

If the return value is a request with an error, calling
[AsyncGPUReadbackRequest.hasError](Rendering.AsyncGPUReadbackRequest-
hasError.html) returns true.  
  
For texture data, the extents are checked against the size of the source
texture. If graphics [QualitySettings](QualitySettings.html) are set low
enough to generate reduced size textures, then the reduced size must be
requested. Use QualitySettings.masterTextureLimit to adjust the width and
height (and x,y if required), by bit shifting right.  
  
For texture data, use the
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) method with
the
[GraphicsFormatUsage.ReadPixels](Experimental.Rendering.GraphicsFormatUsage.ReadPixels.html)
flag to query if the format is supported.  
  
When requesting into multiple slices in the same frame, ensure that each slice
comes from a different memory allocation. Using multiple slices from the same
allocation within a single frame is not supported.

* * *

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output,
[ComputeBuffer](ComputeBuffer.html) src, Action<AsyncGPUReadbackRequest>
callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output,
[ComputeBuffer](ComputeBuffer.html) src, int size, int offset,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output,
[GraphicsBuffer](GraphicsBuffer.html) src, Action<AsyncGPUReadbackRequest>
callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
RequestIntoNativeSlice(ref NativeSlice<T> output,
[GraphicsBuffer](GraphicsBuffer.html) src, int size, int offset,
Action<AsyncGPUReadbackRequest> callback);

### Parameters

output | Reference to the NativeSlice to write the data into. The underlying memory cannot be Disposed until the request is complete.  
---|---  
src | The [GraphicsBuffer](GraphicsBuffer.html) to read the data from.  
size | The size, in bytes, of the data to retrieve from the [GraphicsBuffer](GraphicsBuffer.html).  
offset | Offset in bytes in the [GraphicsBuffer](GraphicsBuffer.html).  
callback | An optional delegate System.Action to call after Unity completes the request. When Unity calls the delegate, it passes the completed request as a parameter to the System.Action.  
  
### Returns

**AsyncGPUReadbackRequest** Returns an
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html) that you can
use to determine when the data is available. Otherwise, returns a request with
an error.

### Description

Retrieves data asynchronously from a GPU Graphics Buffer resource.

If the return value is a request with an error, calling
[AsyncGPUReadbackRequest.hasError](Rendering.AsyncGPUReadbackRequest-
hasError.html) returns true.  
  
For texture data, the extents are checked against the size of the source
texture. If graphics [QualitySettings](QualitySettings.html) are set low
enough to generate reduced size textures, then the reduced size must be
requested. Use QualitySettings.masterTextureLimit to adjust the width and
height (and x,y if required), by bit shifting right.  
  
For texture data, use the
[SystemInfo.IsFormatSupported](SystemInfo.IsFormatSupported.html) method with
the
[GraphicsFormatUsage.ReadPixels](Experimental.Rendering.GraphicsFormatUsage.ReadPixels.html)
flag to query if the format is supported.

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

