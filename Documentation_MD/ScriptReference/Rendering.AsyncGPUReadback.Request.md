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

#  [AsyncGPUReadback](Rendering.AsyncGPUReadback.html).Request

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
Request([ComputeBuffer](ComputeBuffer.html) src,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([GraphicsBuffer](GraphicsBuffer.html) src,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([ComputeBuffer](ComputeBuffer.html) src, int size, int offset,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([GraphicsBuffer](GraphicsBuffer.html) src, int size, int offset,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex,
[TextureFormat](TextureFormat.html) dstFormat, Action<AsyncGPUReadbackRequest>
callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
dstFormat, Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex, int x, int width, int y,
int height, int z, int depth, Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex, int x, int width, int y,
int height, int z, int depth, [TextureFormat](TextureFormat.html) dstFormat,
Action<AsyncGPUReadbackRequest> callback);

## Declaration

public static
[Rendering.AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html)
Request([Texture](Texture.html) src, int mipIndex, int x, int width, int y,
int height, int z, int depth,
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
dstFormat, Action<AsyncGPUReadbackRequest> callback);

### Parameters

src | Resource to read the data from.  
---|---  
size | Size in bytes of the data to be retrieved from the [ComputeBuffer](ComputeBuffer.html) or [GraphicsBuffer](GraphicsBuffer.html).  
offset | Offset in bytes in the [ComputeBuffer](ComputeBuffer.html) or [GraphicsBuffer](GraphicsBuffer.html).  
mipIndex | Index of the mipmap to be fetched.  
dstFormat | Target [TextureFormat](TextureFormat.html) of the data. If the target format is different from the format stored on the GPU, the conversion is automatic.  
x | Starting X coordinate in pixels of the Texture data to be fetched.  
width | Width in pixels of the Texture data to be fetched.  
y | Starting Y coordinate in pixels of the Texture data to be fetched.  
height | Height in pixels of the Texture data to be fetched.  
z | Start Z coordinate in pixels for the [Texture3D](Texture3D.html) being fetched. Index of Start layer for TextureCube, [Texture2DArray](Texture2DArray.html) and TextureCubeArray being fetched.  
depth | Depth in pixels for [Texture3D](Texture3D.html) being fetched. Number of layers for TextureCube, TextureArray and TextureCubeArray.  
callback | An optional delegate System.Action called once the request is fullfilled. The completed request is passed as parameter to the System.Action.  
  
### Returns

**AsyncGPUReadbackRequest** Returns an
[AsyncGPUReadbackRequest](Rendering.AsyncGPUReadbackRequest.html) that you can
use to determine when the data is available. Otherwise, a request with an
error is returned.

### Description

Retrieves data asynchronously from a GPU resource.

If a request with an error is returned, calling
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
  
If you use this function to request data about a temporary render texture,
don't release the texture using
[RenderTexture.ReleaseTemporary](RenderTexture.ReleaseTemporary.html) until
the request is complete.

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

