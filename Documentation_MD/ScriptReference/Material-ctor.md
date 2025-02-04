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

# Material Constructor

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

[Switch to Manual](../Manual/class-Material.html "Go to Material Component in
the Manual")

## Declaration

public Material([Shader](Shader.html) shader);

## Declaration

public Material([Material](Material.html) source);

### Parameters

shader | Create a material with a given [Shader](Shader.html).  
---|---  
source | Create a material by copying all properties from another material.  
  
### Description

Create a temporary Material.

If you have a script which implements a custom special effect, you implement
all the graphic setup using shaders & materials. Use this function to create a
custom shader & material inside your script. After creating the material, use
[SetColor](Material.SetColor.html), [SetTexture](Material.SetTexture.html),
[SetFloat](Material.SetFloat.html), [SetVector](Material.SetVector.html),
[SetMatrix](Material.SetMatrix.html) to populate the shader property values.  
  
Additional resources: [Materials](../Manual/Materials.html),
[Shaders](../Manual/Shaders.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Creates a material from shader and texture references.
        [Shader](Shader.html) shader;
        [Texture](Texture.html) texture;
        [Color](Color.html) color;  
      
        void Start()
        {
            [Renderer](Renderer.html) rend = GetComponent<[Renderer](Renderer.html)> ();  
      
            rend.material = new [Material](Material.html)(shader);
            rend.material.mainTexture = texture;
            rend.material.color = color;
        }
    }
    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Creates a cube and assigns a material with a builtin Specular shader.
        void Start()
        {
            [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            [Renderer](Renderer.html) rend = cube.GetComponent<[Renderer](Renderer.html)> ();
            rend.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
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

