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

#  [Material](Material.html).SetFloat

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

public void SetFloat(string name, float value);

## Declaration

public void SetFloat(int nameID, float value);

### Parameters

nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
---|---  
value | Float value to set.  
name | Property name, e.g. "_Glossiness".  
  
### Description

Sets a named float value.

When setting values on materials using the Standard Shader, you should be
aware that you may need to use [EnableKeyword](Material.EnableKeyword.html) to
enable features of the shader that were not previously in use. For more
detail, read [Accessing Materials via
Script](../Manual/MaterialsAccessingViaScript.html).  
  
Additional resources: [GetFloat](Material.GetFloat.html),
[Materials](../Manual/Materials.html), [ShaderLab
documentation](../Manual/Shaders.html),
[Shader.PropertyToID](Shader.PropertyToID.html), [Properties in Shader
Programs](../Manual/SL-PropertiesInPrograms.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Renderer](Renderer.html) rend;  
      
        void Start()
        {
            rend = GetComponent<[Renderer](Renderer.html)> ();  
      
            // Use the Specular shader on the material
            rend.material.shader = [Shader.Find](Shader.Find.html)("Specular");
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Animate the Shininess value
            float shininess = [Mathf.PingPong](Mathf.PingPong.html)([Time.time](Time-time.html), 1.0f);
            rend.material.SetFloat("_Shininess", shininess);
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

