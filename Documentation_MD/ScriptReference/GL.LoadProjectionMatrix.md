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

#  [GL](GL.html).LoadProjectionMatrix

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

public static void LoadProjectionMatrix([Matrix4x4](Matrix4x4.html) mat);

### Description

Load an arbitrary matrix to the current projection matrix.

This function overrides current camera's projection parameters, so most often
you want to save and restore projection matrix using
[GL.PushMatrix](GL.PushMatrix.html) and [GL.PopMatrix](GL.PopMatrix.html). The
model and view matrix remain unchanged. Beware that the view matrix of the
camera typically performs a scaling of -1 along the z axis, which might have
to be taken into account depending on your use case.  
  
The loaded projection matrix is expected to project into the API-agnostic clip
volume defined by the following boundaries:  
**1.** x = -1..1 (left..right)  
**2.** y = -1..1 (bottom..top)  
**3.** z = -1..1 (near..far)  
  
Unity might combine the matrix with an additional transformation to map to the
convention of the actual graphics API. The resulting matrix can be obtained
through [GL.GetGPUProjectionMatrix](GL.GetGPUProjectionMatrix.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Matrix4x4](Matrix4x4.html) projMtrx = [Matrix4x4.identity](Matrix4x4-identity.html);  
      
        void OnPostRender()
        {
            [GL.PushMatrix](GL.PushMatrix.html)();
            [GL.LoadProjectionMatrix](GL.LoadProjectionMatrix.html)(projMtrx);
            // Do your drawing here...
            [GL.PopMatrix](GL.PopMatrix.html)();
        }
    }
    

Additional resources: [GL.LoadOrtho](GL.LoadOrtho.html).

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

