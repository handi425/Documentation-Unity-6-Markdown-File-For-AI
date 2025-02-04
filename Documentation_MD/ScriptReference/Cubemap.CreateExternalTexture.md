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

#  [Cubemap](Cubemap.html).CreateExternalTexture

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

public static [Cubemap](Cubemap.html) CreateExternalTexture(int width,
[TextureFormat](TextureFormat.html) format, bool mipmap, IntPtr nativeTex);

### Parameters

size | The width and height of each face of the cubemap should be the same.  
---|---  
format | Format of underlying cubemap object.  
mipmap | Does the cubemap have mipmaps?  
nativeTex | Native cubemap texture object.  
  
### Description

Creates a Unity cubemap out of externally created native cubemap object.

This method is mostly useful for [native code plugins](../Manual/native-
plugin-interface.html) that create platform specific cubemap texture objects
outside of Unity, and need to use these cubemaps in Unity Scenes.  
  
Parameters passed to CreateExternalTexture should match what the texture
actually is; and the underlying texture should be a Cubemap (2D textures will
not work).  
  
Native texture object on Direct3D-like devices is a pointer to the base type,
from which a texture can be created (ID3D11ShaderResourceView on D3D11). On
OpenGL/OpenGL ES it is GLuint. On Metal it is id<MTLTexture>.  
  
Additional resources:
[UpdateExternalTexture](Cubemap.UpdateExternalTexture.html),
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

