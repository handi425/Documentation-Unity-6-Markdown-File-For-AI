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

#  [Canvas](Canvas.html).additionalShaderChannels

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

public [AdditionalCanvasShaderChannels](AdditionalCanvasShaderChannels.html)
additionalShaderChannels;

### Description

Get or set the mask of additional shader channels to be used when creating the
[Canvas](Canvas.html) mesh.

The [Canvas](Canvas.html) will always include Position, Color, and Uv0 shader
channels when generating the mesh for a overlay [Canvas](Canvas.html) and will
also include Normal and Tangent for ScreenSpace.Camera and World space
[Canvas](Canvas.html). These are the optional additional parameters to be
copied.

    
    
    using UnityEngine;  
      
    public class SetCanvasShaderChannels : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Canvas](Canvas.html) canvas;  
      
        void Start()
        {
            canvas.additionalShaderChannels |= [AdditionalCanvasShaderChannels.Normal](AdditionalCanvasShaderChannels.Normal.html);
            canvas.additionalShaderChannels |= [AdditionalCanvasShaderChannels.TexCoord1](AdditionalCanvasShaderChannels.TexCoord1.html);
            canvas.additionalShaderChannels |= [AdditionalCanvasShaderChannels.Tangent](AdditionalCanvasShaderChannels.Tangent.html);
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

