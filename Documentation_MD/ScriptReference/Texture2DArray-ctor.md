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

# Texture2DArray Constructor

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

[Switch to Manual](../Manual/class-Texture2DArray.html "Go to Texture2DArray
Component in the Manual")

## Declaration

public Texture2DArray(int width, int height, int depth,
[TextureFormat](TextureFormat.html) textureFormat, bool mipChain, bool linear
= false);

## Declaration

public Texture2DArray(int width, int height, int depth,
[TextureFormat](TextureFormat.html) textureFormat, bool mipChain, bool linear
= false, bool createUninitialized = false);

## Declaration

public Texture2DArray(int width, int height, int depth,
[TextureFormat](TextureFormat.html) textureFormat, int mipCount, bool linear);

## Declaration

public Texture2DArray(int width, int height, int depth,
[TextureFormat](TextureFormat.html) textureFormat, int mipCount, bool linear,
bool createUninitialized);

## Declaration

public Texture2DArray(int width, int height, int depth,
[TextureFormat](TextureFormat.html) textureFormat, int mipCount, bool linear,
bool createUninitialized, [MipmapLimitDescriptor](MipmapLimitDescriptor.html)
mipmapLimitDescriptor);

### Parameters

width | Width of texture array in pixels.  
---|---  
height | Height of texture array in pixels.  
depth | Number of elements in the texture array.  
linear | Does the texture contain non-color data (i.e. don't do any color space conversions when sampling)? Default is false.  
textureFormat | Format of the texture.  
mipChain | Should mipmaps be created?  
mipCount | Amount of mips to allocate for the texture array.  
createUninitialized | Use this flag to create the texture with uninitialized data. When overriding all texels anyway, this can lead to improved performance and reduced memory usage.  
mipmapLimitDescriptor | Determines whether the texture uses a mipmap limit, and which mipmap limit to use. See [MipmapLimitDescriptor](MipmapLimitDescriptor.html)  
  
### Description

Create a new texture array.

Enable `createUninitialized` to make the texture reference uninitialized data
(both on the CPU and GPU). When overriding all texels, this can lead to
improved performance and reduced memory usage during construction. Note that
sampling an uninitialized texture gives unpredictable values.  
  
Usually you will want to set the colors of the texture after creating it. Use
[SetPixels](Texture2DArray.SetPixels.html),
[SetPixels32](Texture2DArray.SetPixels32.html) or
[Graphics.CopyTexture](Graphics.CopyTexture.html) functions for that.  
  
Note that this class does not support Texture2DArray creation with a Crunch
compression [TextureFormat](TextureFormat.html).  
  
When you enable mipmap limits with a `mipmapLimitDescriptor`, a readable CPU
copy is required for the texture to reupload when quality settings change. If
the texture is made nonreadable (see
[Texture2DArray.Apply](Texture2DArray.Apply.html)), the uploaded resolution
will no longer adapt to the active quality level.

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

