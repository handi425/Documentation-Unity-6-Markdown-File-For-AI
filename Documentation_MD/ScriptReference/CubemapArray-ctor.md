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

# CubemapArray Constructor

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

[Switch to Manual](../Manual/class-CubemapArray.html "Go to CubemapArray
Component in the Manual")

## Declaration

public CubemapArray(int width, int cubemapCount,
[TextureFormat](TextureFormat.html) textureFormat, bool mipChain);

## Declaration

public CubemapArray(int width, int cubemapCount,
[TextureFormat](TextureFormat.html) textureFormat, bool mipChain, bool linear
= false, bool createUninitialized = false);

## Declaration

public CubemapArray(int width, int cubemapCount,
[TextureFormat](TextureFormat.html) textureFormat, int mipCount, bool linear);

## Declaration

public CubemapArray(int width, int cubemapCount,
[TextureFormat](TextureFormat.html) textureFormat, int mipCount, bool linear,
bool createUninitialized = false);

### Parameters

cubemapCount | Number of elements in the cubemap array.  
---|---  
linear | Does the texture contain non-color data (i.e. don't do any color space conversions when sampling)? Default is false.  
width | Width of each cubemap face.  
textureFormat | Format of the cubemaps.  
mipChain | Should mipmaps be generated ?  
mipCount | Amount of mipmaps to generate.  
createUninitialized | Use this flag to create the texture with uninitialized data. When overriding all texels anyway, this can lead to improved performance and reduced memory usage.  
  
### Description

Create a new cubemap array.

Enable `createUninitialized` to make the texture reference uninitialized data
(both on the CPU and GPU). When overriding all texels, this can lead to
improved performance and reduced memory usage during construction. Note that
sampling an uninitialized texture gives unpredictable values.  
  
Usually you will want to set the colors of the cubemaps after creating it. Use
[SetPixels](CubemapArray.SetPixels.html),
[SetPixels32](CubemapArray.SetPixels32.html) or
[Graphics.CopyTexture](Graphics.CopyTexture.html) functions for that.  
  
Note that this class does not support CubemapArray creation with a Crunch
compression [TextureFormat](TextureFormat.html).

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

