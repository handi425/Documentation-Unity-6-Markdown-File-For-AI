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

#  [MaterialPropertyBlock](MaterialPropertyBlock.html).Clear

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

public void Clear();

### Description

Clear material property values.

[Graphics.RenderMesh](Graphics.RenderMesh.html) copies the passed property
block, so the most efficient way of using it is to create one block and reuse
it for all DrawMesh calls. Use [Clear](MaterialPropertyBlock.Clear.html) to
clear block's values, and [SetFloat](MaterialPropertyBlock.SetFloat.html),
[SetVector](MaterialPropertyBlock.SetVector.html),
[SetColor](MaterialPropertyBlock.SetColor.html),
[SetMatrix](MaterialPropertyBlock.SetMatrix.html) to add values.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Mesh](Mesh.html) aMesh;
        [Material](Material.html) aMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("VertexLit"));  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [MaterialPropertyBlock](MaterialPropertyBlock.html) materialProperty = new [MaterialPropertyBlock](MaterialPropertyBlock.html)();  
      
            // Clear any property and add a red color
            materialProperty.Clear();
            materialProperty.SetColor("_Color", [Color.red](Color-red.html));
            [Graphics.DrawMesh](Graphics.DrawMesh.html)(aMesh, new [Vector3](Vector3.html)(5, 0, 0),
                [Quaternion.identity](Quaternion-identity.html), aMaterial, 0, null, 0, materialProperty);  
      
            // Clear any property and add a green color
            materialProperty.Clear();
            materialProperty.SetColor("_Color", [Color.green](Color-green.html));
            [Graphics.DrawMesh](Graphics.DrawMesh.html)(aMesh, new [Vector3](Vector3.html)(-5, 0, 0),
                [Quaternion.identity](Quaternion-identity.html), aMaterial, 0, null, 0, materialProperty);
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

