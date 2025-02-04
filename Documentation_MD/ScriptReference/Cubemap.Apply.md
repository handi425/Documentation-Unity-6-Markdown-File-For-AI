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

#  [Cubemap](Cubemap.html).Apply

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

public void Apply(bool updateMipmaps = true, bool makeNoLongerReadable =
false);

### Parameters

updateMipmaps | When the value is `true`, Unity recalculates mipmap levels, using mipmap level 0 as the source. The default value is `true`.  
---|---  
makeNoLongerReadable | When the value is `true`, Unity deletes the texture in CPU memory after it uploads it to the GPU, and sets [isReadable](Texture-isReadable.html) to `false`. The default value is `false`.  
  
### Description

Copies changes you've made in a CPU texture to the GPU.

For most types of textures, Unity can store a copy of the texture in both CPU
and GPU memory.  
  
The CPU copy is optional. If the CPU copy exists, you can read from and write
to the CPU copy more flexibly than the GPU copy. But to render the updated
texture, you must use `Apply` to copy it from the CPU to the GPU.  
  
If you set `makeNoLongerReadable` to `true`, Unity deletes the CPU copy of the
texture after it uploads it to the GPU.  
  
You usually only set `updateMipmaps` to `false` if you've already updated the
mipmap levels, for example using [SetPixels](Cubemap.SetPixels.html).  
  
`Apply` is an expensive operation because it copies all the pixels in the
texture even if you've only changed some of the pixels, so change as many
pixels as possible before you call it.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Cubemap](Cubemap.html) cubeMap;  
      
        void Start()
        {
            cubeMap.SetPixel([CubemapFace.PositiveX](CubemapFace.PositiveX.html), 0, 0, [Color.red](Color-red.html));
            // Do more changes to the faces...
            cubeMap.Apply(); // Apply the stuff done to the [Cubemap](Cubemap.html).
        }
    }
    

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

