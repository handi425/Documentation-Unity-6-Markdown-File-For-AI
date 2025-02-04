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

#  [MaterialPropertyBlock](MaterialPropertyBlock.html).SetColor

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

public void SetColor(string name, [Color](Color.html) value);

## Declaration

public void SetColor(int nameID, [Color](Color.html) value);

### Parameters

name | The name of the property.  
---|---  
nameID | The name ID of the property retrieved by [Shader.PropertyToID](Shader.PropertyToID.html).  
value | The [Color](Color.html) value to set.  
  
### Description

Set a color property.

Adds a property to the block. If a color property with the given name already
exists, the old value is replaced.  
  
The color value is considered to be always set in sRGB space and is converted
to linear if the active color space is linear. You need manual updating of the
color value if you switch between color spaces.

    
    
    using UnityEngine;  
      
    // Draws 3 meshes with the same material but with different colors.
    using UnityEngine;
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;
        public [Material](Material.html) material;
        private [MaterialPropertyBlock](MaterialPropertyBlock.html) block;  
      
        void Start()
        {
            block = new [MaterialPropertyBlock](MaterialPropertyBlock.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // setup render params
            [RenderParams](RenderParams.html) rp = new [RenderParams](RenderParams.html)(material) {matProps = block};  
      
            // red mesh
            block.SetColor("_Color", [Color.red](Color-red.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(0, 0, 0)));  
      
            // green mesh
            block.SetColor("_Color", [Color.green](Color-green.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(5, 0, 0)));  
      
            // blue mesh
            block.SetColor("_Color", [Color.blue](Color-blue.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(-5, 0, 0)));
        }
    }
    

Function variant that takes `nameID` is faster. If you are changing properties
with the same name repeatedly, use
[Shader.PropertyToID](Shader.PropertyToID.html) to get unique identifier for
the name, and pass the identifier to SetColor.

    
    
    using UnityEngine;  
      
    // Draws 3 meshes with the same material but with different colors.
    using UnityEngine;
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;
        public [Material](Material.html) material;
        private [MaterialPropertyBlock](MaterialPropertyBlock.html) block;  
      
        void Start()
        {
            block = new [MaterialPropertyBlock](MaterialPropertyBlock.html)();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // setup render params
            [RenderParams](RenderParams.html) rp = new [RenderParams](RenderParams.html)(material) {matProps = block};  
      
            // red mesh
            block.SetColor("_Color", [Color.red](Color-red.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(0, 0, 0)));  
      
            // green mesh
            block.SetColor("_Color", [Color.green](Color-green.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(5, 0, 0)));  
      
            // blue mesh
            block.SetColor("_Color", [Color.blue](Color-blue.html));
            [Graphics.RenderMesh](Graphics.RenderMesh.html)(rp, mesh, 0, [Matrix4x4.Translate](Matrix4x4.Translate.html)(new [Vector3](Vector3.html)(-5, 0, 0)));
        }
    }
    

Additional resources: [SetFloat](MaterialPropertyBlock.SetFloat.html),
[SetVector](MaterialPropertyBlock.SetVector.html),
[SetMatrix](MaterialPropertyBlock.SetMatrix.html),
[SetTexture](MaterialPropertyBlock.SetTexture.html).

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

