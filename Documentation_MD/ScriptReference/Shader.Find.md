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

#  [Shader](Shader.html).Find

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

[Switch to Manual](../Manual/class-Shader.html "Go to Shader Component in the
Manual")

## Declaration

public static [Shader](Shader.html) Find(string name);

### Description

Finds a shader with the given `name`. Returns `null` if the shader is not
found.

Shader.Find can be used to switch to another shader without having to keep a
reference to the shader. `name` is the name you can see in the shader popup of
any material, for example "Standard", "Unlit/Texture", "Legacy
Shaders/Diffuse" etc.  
  
Note that a shader might be not included into the player build if nothing
references it. In that case, Shader.Find will work only in the Editor, and
will result in the pink [error shader](../Manual/shader-error.html) in a
build. Because of that, it is advisable to use shader references instead of
finding them by name. To make sure a shader is included into the game build,
do either of: 1) reference it from some of the materials used in your Scene,
2) add it under "Always Included Shaders" list in ProjectSettings/Graphics or
3) put shader or something that references it (e.g. a Material) into a
"Resources" folder.  
  
Additional resources: [Material](Material.html) class.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Create a material from code
        void Start()
        {
            // Create a material with transparent diffuse shader
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Transparent/Diffuse"));
            material.color = [Color.green](Color-green.html);  
      
            // assign the material to the renderer
            GetComponent<[Renderer](Renderer.html)>().material = material;
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

