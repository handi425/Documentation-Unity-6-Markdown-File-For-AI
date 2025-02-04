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

#  [SystemInfo](SystemInfo.html).graphicsShaderLevel

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

public static int graphicsShaderLevel;

### Description

Graphics device shader capability level (Read Only).

This is approximate "shader capability" level of the graphics device,
expressed in DirectX shader model terms. Possible values are:  
  
**50** Shader Model 5.0 (DX11.0)  
**46** OpenGL 4.1 capabilities (Shader Model 4.0 + tessellation)  
**45** Metal / OpenGL ES 3.1 capabilities (Shader Model 3.5 + compute shaders)  
**40** Shader Model 4.0 (DX10.0)  
**35** OpenGL ES 3.0 capabilities (Shader Model 3.0 + integers, texture
arrays, instancing)  
**30** Shader Model 3.0  
**25** Shader Model 2.5 (DX11 feature level 9.3 feature set)  
**20** Shader Model 2.0.  
  
Additional resources: [shader compilation targets](../Manual/SL-
ShaderCompileTargets.html).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Check for shader model 4.5 or better support
            if ([SystemInfo.graphicsShaderLevel](SystemInfo-graphicsShaderLevel.html) >= 45)
                print("Woohoo, decent shaders supported!");
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

