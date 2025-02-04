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

#  [Shader](Shader.html).SetGlobalFloat

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

public static void SetGlobalFloat(string name, float value);

## Declaration

public static void SetGlobalFloat(int nameID, float value);

### Parameters

nameID | The name ID of the property retrieved by [Shader.PropertyToID](Shader.PropertyToID.html).  
---|---  
name | The name of the property.  
  
### Description

Sets a global float property for all shaders.

Global properties are used if a shader needs them but the material does not
have them defined (for example, if the shader does not expose them in
`Properties` block).  
  
Usually this is used if you have a set of custom shaders that all use the same
"global" float (for example, density of some custom fog type). Then you can
set the global property from script and don't have to setup the same float in
all materials.  
  
Additional resources: [SetGlobalColor](Shader.SetGlobalColor.html),
[SetGlobalTexture](Shader.SetGlobalTexture.html); [Material](Material.html)
class, [ShaderLab documentation](../Manual/Shaders.html).  
  
The following example sets the global float property `_MyFloat` to `1` in all
shaders.

    
    
    using UnityEngine;  
      
    public class SetGlobalFloatExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Shader.SetGlobalFloat](Shader.SetGlobalFloat.html)("_MyFloat", 1.0f);
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

