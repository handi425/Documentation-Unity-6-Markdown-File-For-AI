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

#  [RenderTexture](RenderTexture.html).Create

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

[Switch to Manual](../Manual/class-RenderTexture.html "Go to RenderTexture
Component in the Manual")

## Declaration

public bool Create();

### Returns

**bool** True if the texture is created, else false.

### Description

Actually creates the RenderTexture.

RenderTexture constructor does not actually create the hardware texture; by
default the texture is created the first time it is set
[active](RenderTexture-active.html). Calling `Create` lets you create it up
front. `Create` does nothing if the texture is already created.  
  
The initial contents of a newly created render texture are undefined. On some
platforms and APIs the contents will default to black, but you shouldn't
depend on this. You can use
[LoadStoreActionDebugModeSettings](Rendering.LoadStoreActionDebugModeSettings.html)
to highlight undefined areas of the display, to help you debug rendering
problems on mobile platforms.  
  
Additional resources: [Release](RenderTexture.Release.html),
[IsCreated](RenderTexture.IsCreated.html) functions.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [RenderTexture](RenderTexture.html) rt;  
      
        void  Start()
        {
            rt = new [RenderTexture](RenderTexture.html)(256, 256, 16, [RenderTextureFormat.ARGB32](RenderTextureFormat.ARGB32.html));
            rt.Create();  
      
            // Add code here to work on the render texture  
      
            // Release the hardware resources used by the render texture
            rt.Release();
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

