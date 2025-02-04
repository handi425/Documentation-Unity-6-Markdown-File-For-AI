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

#  [GL](GL.html).invertCulling

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

public static bool invertCulling;

### Description

Select whether to invert the backface culling (true) or not (false).

This flag can "flip" the culling mode of all rendered objects. Major use case:
rendering reflections for mirrors, water etc. Since virtual camera for
rendering the reflection is mirrored, the culling order has to be inverted.
You can see how the Water script in Effects standard package does that.

    
    
    // When attached to the camera, this script
    // will make all rendering be flipped "inside out",
    // i.e. back faces of objects will be rendered instead
    // of front faces.
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private bool oldCulling;
        public void OnPreRender()
        {
            oldCulling = [GL.invertCulling](GL-invertCulling.html);
            [GL.invertCulling](GL-invertCulling.html) = true;
        }  
      
        public void OnPostRender()
        {
            [GL.invertCulling](GL-invertCulling.html) = oldCulling;
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

