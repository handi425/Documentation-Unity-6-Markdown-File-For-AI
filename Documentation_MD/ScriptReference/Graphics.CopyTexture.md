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

#  [Graphics](Graphics.html).CopyTexture

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

public static void CopyTexture([Texture](Texture.html) src,
[Texture](Texture.html) dst);

## Declaration

public static void CopyTexture([Texture](Texture.html) src, int srcElement,
int srcMip, [Texture](Texture.html) dst, int dstElement, int dstMip);

## Declaration

public static void CopyTexture([Texture](Texture.html) src, int srcElement,
int srcMip, int srcX, int srcY, int srcWidth, int srcHeight,
[Texture](Texture.html) dst, int dstElement, int dstMip, int dstX, int dstY);

## Declaration

public static void
CopyTexture([Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) src,
[Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) dst);

## Declaration

public static void
CopyTexture([Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) src,
int srcElement, int srcMip,
[Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) dst, int
dstElement, int dstMip);

## Declaration

public static void
CopyTexture([Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) src,
int srcElement, int srcMip, int srcX, int srcY, int srcWidth, int srcHeight,
[Rendering.GraphicsTexture](Rendering.GraphicsTexture.html) dst, int
dstElement, int dstMip, int dstX, int dstY);

### Parameters

src | The source texture.  
---|---  
dst | The destination texture.  
srcElement | The element in the source texture to copy from. For example, the [CubemapFace](CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `src` is a 2D texture.  
srcMip | The mipmap level to copy from. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html) or [GraphicsTextureDescriptor.mipCount](Rendering.GraphicsTextureDescriptor-mipCount.html). The default value is `0`.  
dstElement | The element in the destination texture to copy to. For example, the [CubemapFace](CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `dst` is a 2D texture.  
dstMip | The mipmap level to write to. The range is `0` through the texture's [Texture.mipmapCount](Texture-mipmapCount.html) or [GraphicsTextureDescriptor.mipCount](Rendering.GraphicsTextureDescriptor-mipCount.html). The default value is `0`.  
srcX | The starting x coordinate of `src` to copy from. `0` is the left of the texture.  
srcY | The starting y coordinate of `src` to copy from. `0` is the bottom of the texture.  
srcWidth | The width of `src` to copy.  
srcHeight | The height of `src` to copy.  
dstX | The x coordinate of `dst` to copy to.  
dstY | The y coordinate to `dst` to copy to.  
  
### Description

Copies pixel data from one texture to another.

This method copies pixel data from one texture to another on the GPU. If you
set [Texture.isReadable](Texture-isReadable.html) to `true` for both `src` and
`dst` [Texture](Texture.html) parameters, the method also attempts to copy
pixel data on the CPU by running `CopyPixels` on the `dst` texture.  
  
If you set [Texture.isReadable](Texture-isReadable.html) to `false` or use
[GraphicsTexture](Rendering.GraphicsTexture.html) for the `src` and `dst`,
pixel data will not be copied on the CPU and `CopyTexture` becomes one of the
fastest ways to copy a texture. But to use `CopyTexture`, the following must
be the same in both the source and destination texture areas:

  * Format. You can also use two compatible formats - for example, [TextureFormat.ARGB32](TextureFormat.ARGB32.html) and [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html).
  * Size.
  * [RenderTexture.antiAliasing](RenderTexture-antiAliasing.html) or [GraphicsTextureDescriptor.numSamples](Rendering.GraphicsTextureDescriptor-numSamples.html) values, if the textures are render targets.

You might be able to copy between incompatible formats depending on your
graphics API. For example, on some APIs you can copy between formats with the
same bit width.  
  
Depending on your graphics API, you might not be able to copy between
different types of textures. For more information on compatibility, see
[SystemInfo.copyTextureSupport](SystemInfo-copyTextureSupport.html) and
[CopyTextureSupport](Rendering.CopyTextureSupport.html).  
  
If `src` is a depth-only render target, you must copy the whole texture, not
part of it. A depth-only render texture has its color buffer set to a [color
format](RenderTexture-graphicsFormat.html) of `None` and its depth buffer set
to a valid [RenderTexture.depthStencilFormat](RenderTexture-
depthStencilFormat.html). A depth graphics texture has its
[format](Rendering.GraphicsTextureDescriptor-format.html) set to a valid
[GraphicsFormat](Experimental.Rendering.GraphicsFormat.html) with a depth
component.  
  
When you use [QualitySettings.globalTextureMipmapLimit](QualitySettings-
globalTextureMipmapLimit.html),
[Texture2D.mipmapLimitGroup](Texture2D-mipmapLimitGroup.html) and
[Texture2D.ignoreMipmapLimit](Texture2D-ignoreMipmapLimit.html), textures can
have a variety of mipmap limit settings. This means you may not be able to
copy from one mipmap level to another, because for example the source texture
is limited to half resolution and the destination texture is limited to
quarter resolution. Note that this does not apply when `src` and `dst` are set
to graphics textures, because graphics textures already have their mipmap
count limited, and only represent the mipmap levels that are currently
uploaded.  
  
If you need to copy a mip between textures with different mipmap limit
settings, use the region-based overload. This overload adjusts the source
rectangle based on the source texture's mipmap limit settings, and the
destination offset based on the destination's mipmap limit settings. For
example, copying a 128x128 area from position 16,16 to position 32,32 results
in a variety of behaviors based on the global texture mipmap limit, the source
texture type, and the destination texture type:

  * When the global texture mipmap limit is 0, and both textures are subject to it, Unity performs all copies as expected.
  * When the global texture mipmap limit is 2, and both textures are subject to it, Unity adjusts the source rectangle to 32x32 and its offset to 4,4, then changes the destination offset to 8x8. Unity then performs all copies as expected and ignores all mipmap limit settings.
  * When the global texture mipmap limit is 2, the source is a texture subject to it, and the destination is a texture not subject to it, Unity adjusts the source rectangle to 32x32 and its offset to 4,4, but doesn't change the destination offset, which remains 32x32.

The following sample shows how you can copy to or from a Texture2DArray, when
Texture2Ds have mipmap limits:

    
    
    using UnityEngine;  
      
    public class CopyTextureSample : [MonoBehaviour](MonoBehaviour.html)
    {
        // [Sample](PackageManager.UI.Sample.html) to copy all available mips: inTex -> outArray (no mipmap limits) -> outTex
        [[SerializeField](SerializeField.html)] [Texture2D](Texture2D.html) inTex;
        [[SerializeField](SerializeField.html)] [Texture2DArray](Texture2DArray.html) outArray;
        [[SerializeField](SerializeField.html)] [Texture2D](Texture2D.html) outTex;
        [[SerializeField](SerializeField.html)] bool considerMipmapLimits;  
      
        void Start()
        {
            int width = inTex.width;
            int height = inTex.width;  
      
            outArray = new [Texture2DArray](Texture2DArray.html)(width, height, 1, inTex.format, true);
            outTex = new [Texture2D](Texture2D.html)(width, height, inTex.format, true);  
      
            if (!considerMipmapLimits)
            {
                // [Texture2D](Texture2D.html) -> [Texture2DArray](Texture2DArray.html)
                // Global Mipmap Limit: "1: Half [Resolution](Resolution.html)" => copies into mips that are now too large; will copy each mip of inTex into a quarter of outArray
                for (int mip = 0; mip < inTex.mipmapCount; ++mip)
                {
                    int copyWidth = width >> mip;
                    int copyHeight = height >> mip;
                    [Graphics.CopyTexture](Graphics.CopyTexture.html)(inTex, 0, mip, 0, 0, copyWidth, copyHeight, outArray, 0, mip, 0, 0);
                }  
      
                // [Texture2DArray](Texture2DArray.html) -> [Texture2D](Texture2D.html)
                // Global Mipmap Limit: "1: Half [Resolution](Resolution.html)" => errors, since we try to copy into mips that are now too small
                for (int mip = 0; mip < outArray.mipmapCount; ++mip)
                {
                    int copyWidth = width >> mip;
                    int copyHeight = height >> mip;
                    [Graphics.CopyTexture](Graphics.CopyTexture.html)(outArray, 0, mip, 0, 0, copyWidth, copyHeight, outTex, 0, mip, 0, 0);
                }
            }
            else // considering mipmap limits
            {
                int globalMipmapLimit = [QualitySettings.globalTextureMipmapLimit](QualitySettings-globalTextureMipmapLimit.html);  
      
                // [Texture2D](Texture2D.html) -> [Texture2DArray](Texture2DArray.html)
                // Global Mipmap Limit: "1: Half [Resolution](Resolution.html)" => mip0 of outArray is not written to, other mips copy as expected
                //  (ALTERNATIVE: if outArray creation already considered globalMipmapLimit for its dimensions,
                //   the CopyTexture call can ignore globalMipmapLimit since the mips will line up again)
                for (int mip = 0; mip < inTex.mipmapCount - globalMipmapLimit; ++mip)
                {
                    int copyWidth = width >> mip;
                    int copyHeight = height >> mip;
                    int srcMip = mip;
                    int dstMip = mip + globalMipmapLimit;
                    [Graphics.CopyTexture](Graphics.CopyTexture.html)(inTex, 0, srcMip, 0, 0, copyWidth, copyHeight, outArray, 0, dstMip, 0, 0);
                }  
      
                // [Texture2DArray](Texture2DArray.html) -> [Texture2D](Texture2D.html)
                // Global Mipmap Limit: "1: Half [Resolution](Resolution.html)" => mip0 of outArray is not copied (but outTex does not upload it to GPU anyway)
                for (int mip = globalMipmapLimit; mip < outArray.mipmapCount; ++mip)
                {
                    int copyWidth = width >> mip;
                    int copyHeight = height >> mip;
                    int srcMip = mip;
                    int dstMip = mip - globalMipmapLimit;
                    [Graphics.CopyTexture](Graphics.CopyTexture.html)(outArray, 0, srcMip, 0, 0, copyWidth, copyHeight, outTex, 0, dstMip, 0, 0);
                }
            }
        }
    }
    

Mipmap level arguments always refer to a texture's currently loaded mipmap
levels (which can be found via
[GraphicsTextureDescriptor.mipCount](Rendering.GraphicsTextureDescriptor-
mipCount.html) for that texture's [Texture.graphicsTexture](Texture-
graphicsTexture.html)). For example, if the global texture mipmap limit is set
to 0, mip 1 of a 256x256 texture refers to a 128x128 mip. However, for that
same texture, if the global texture mipmap limit is set to 1, mip 1 refers to
a 64x64 mip. If the global texture mipmap limit is set to 2, mip 1 of that
same texture would refer to a 32x32 mip (and so on).  
  
This means that when you use `CopyTexture`, you do not need to take mipmap
limit settings into account in your calls in most cases. However, if you use
[Textures](Texture.html) and the source and destination's mipmap limit
settings differ, you need to adjust for those settings. Keep in mind that
non-2D texture types are always uploaded to the GPU at full resolution,
because they do not support mipmap limit settings of any sort.  
  
Compressed texture formats add some restrictions to the CopyTexture with a
region variant. For example, PVRTC formats are not supported since they are
not block-based (for these formats you can only copy whole texture or whole
mip level). For block-based formats (e.g. DXT, BCn, ETC), the region size and
coordinates must be a multiple of compression block size (4 pixels for DXT).  
  
Even if you set `Texture.isReadable` to true, this method doesn't copy pixel
data on the CPU if you copy only a region of a compressed texture.  
  
Don't use an `Apply` method such as [Texture2D.Apply](Texture2D.Apply.html)
after `CopyTexture`, because you might copy old or undefined CPU texture data
to the GPU.  
  
Additional resources: [CopyTextureSupport](Rendering.CopyTextureSupport.html),
[Texture2D.CopyPixels](Texture2D.CopyPixels.html).

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

