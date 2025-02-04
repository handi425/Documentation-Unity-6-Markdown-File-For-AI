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

#  [Material](Material.html).SetColor

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

public void SetColor(string name, [Color](Color.html) value);

## Declaration

public void SetColor(int nameID, [Color](Color.html) value);

### Parameters

nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
---|---  
name | Property name. For example, "_Color" in Built-in Render Pipeline, "_BaseColor" in URP.  
value | Color value to set.  
  
### Description

Sets a color value.

Many shaders use more than one color. Use SetColor to change the color
(identified by shader property name, or unique property name ID).  
  
When setting color values on materials using the Standard Shader, you should
be aware that you may need to use [EnableKeyword](Material.EnableKeyword.html)
to enable features of the shader that were not previously in use. For more
detail, read [Accessing Materials via
Script](../Manual/MaterialsAccessingViaScript.html).  
  
Color property names are defined in the `Properties` section in the shader
code. Here are examples of the color properties in Unity pre-built shaders:  
`_Color`: the main color of a material (URP: `_BaseColor`). You can access
this shader property via the [color](Material-color.html) property.  
`_EmissionColor`: the emissive color of a material.  
  
Additional resources: [color](Material-color.html),
[GetColor](Material.GetColor.html),
[Shader.PropertyToID](Shader.PropertyToID.html), [Properties in Shader
Programs](../Manual/SL-PropertiesInPrograms.html).

    
    
    //Attach this script to any [GameObject](GameObject.html) in your scene to spawn a cube and change the material color
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
       void Start()
       {
           // Create a new cube primitive to set the color on
           [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));  
      
           // Get the [Renderer](Renderer.html) component from the new cube
           var cubeRenderer = cube.GetComponent<[Renderer](Renderer.html)>();  
      
           // Use SetColor to set the main color shader property
           cubeRenderer.material.SetColor("_Color", [Color.red](Color-red.html));
           // If your project uses URP, uncomment the following line and use it instead of the previous line
           // cubeRenderer.material.SetColor("_BaseColor", [Color.red](Color-red.html));
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

