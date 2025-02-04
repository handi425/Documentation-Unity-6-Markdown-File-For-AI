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

#  [Texture3D](Texture3D.html).CreateExternalTexture

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

[Switch to Manual](../Manual/class-Texture3D.html "Go to Texture3D Component
in the Manual")

## Declaration

public static [Texture3D](Texture3D.html) CreateExternalTexture(int width, int
height, int depth, [TextureFormat](TextureFormat.html) format, bool mipChain,
IntPtr nativeTex);

### Parameters

nativeTex | Native 3D texture object.  
---|---  
width | Width of texture in pixels.  
height | Height of texture in pixels.  
depth | Depth of texture in pixels  
format | Format of underlying texture object.  
mipmap | Does the texture have mipmaps?  
  
### Description

Creates Unity Texture out of externally created native texture object.

This function is mostly useful for [native code plugins](../Manual/native-
plugin-interface.html) that create platform specific texture objects outside
of Unity, and need to use these textures in Unity Scenes. It is also possible
to create a texture in Unity and get a pointer to the underlying platform
representation; see
[Texture.GetNativeTexturePtr](Texture.GetNativeTexturePtr.html).  
  
Parameters passed to CreateExternalTexture should match what the texture
actually is; and the underlying texture should be 3D.  
  
Native texture object on **Direct3D** -like devices is a pointer to the base
type, from which a texture can be created:  
  
• **D3D11** : `ID3D11ShaderResourceView*` or `ID3D11Texture3D*`  
• **D3D12** : `ID3D12Texture3D*`  
  
On **OpenGL** /**OpenGL ES** it is `GLuint`.  
  
On **Metal** it is `id<MTLTexture>`.  
  
For **Vulkan** , the `nativeTex` parameter is a `VkImage*`.  
  
Additional resources:
[UpdateExternalTexture](Texture3D.UpdateExternalTexture.html),
[Texture.GetNativeTexturePtr](Texture.GetNativeTexturePtr.html).

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

