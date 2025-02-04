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

#
[IPreprocessComputeShaders](Build.IPreprocessComputeShaders.html).OnProcessComputeShader

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

public void OnProcessComputeShader([ComputeShader](ComputeShader.html) shader,
string kernelName, IList<ShaderCompilerData> data);

### Parameters

shader | The compute shader that Unity is about to compile.  
---|---  
kernelName | The name of the kernel that Unity is about to compile.  
data | The list of shader variants that Unity is about to compile.  
  
### Description

Implement this interface to receive a callback before Unity compiles a compute
shader kernel into a build.

Use this callback to examine the compute shader variants that Unity is about
to compile into your build, and exclude any variant that you do not want.
Excluding unwanted shader variants can reduce build size and build times.  
  
Variants are represented by
[ShaderCompilerData](Rendering.ShaderCompilerData.html) structs. For each
variant, you can check whether given global or local keywords are enabled
using [ShaderKeywordSet.IsEnabled](Rendering.ShaderKeywordSet.IsEnabled.html).  
  
To check whether a variant has a global keyword enabled, create a
[ShaderKeyword](Rendering.ShaderKeyword.html) instance with the name of the
global keyword. To check whether a variant has a local keyword enabled, create
a [ShaderKeyword](Rendering.ShaderKeyword.html) instance with the name of the
local keyword and an additional parameter that specifies the compute shader
that uses the local keyword.  
  
To exclude a shader variant from the build, directly remove the elements from
`data` . Note that removing elements individually in a for loop can be slow;
if you are removing a lot of elements, consider moving the unwanted elements
to the end of the List and then removing them all in a single operation.  
  
Note that this callback only provides details of compute shaders. To see
regular shaders that Unity is about to compile into the build, see
[IPreprocessShaders](Build.IPreprocessShaders.html) .  
  
This callback is invoked for both Player and AssetBundle builds.  
  
Additional resources: [Shader variants and keywords](../Manual/shader-
variants-and-keywords.html), [Declaring and using shader keywords in
HLSL](../Manual/SL-MultipleProgramVariants.html),
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html),
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html).

    
    
    using System.Collections.Generic;
    using UnityEditor.Build;
    using UnityEditor.Rendering;
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    class MyCustomBuildProcessor : [IPreprocessComputeShaders](Build.IPreprocessComputeShaders.html)
    {
        [ShaderKeyword](Rendering.ShaderKeyword.html) m_GlobalKeywordBlue;  
      
        public MyCustomBuildProcessor()
        {
            // Global keywords are shader agnostic so they can be initialized early
            m_GlobalKeywordBlue = new [ShaderKeyword](Rendering.ShaderKeyword.html)("_BLUE");
        }  
      
        public int callbackOrder { get { return 0; } }  
      
        public void OnProcessComputeShader([ComputeShader](ComputeShader.html) shader, string kernelName, IList<[ShaderCompilerData](Rendering.ShaderCompilerData.html)> data)
        {
            // Local keywords are initialized here as their constructor needs to specify the shader
            [ShaderKeyword](Rendering.ShaderKeyword.html) localKeywordRed = new [ShaderKeyword](Rendering.ShaderKeyword.html)(shader, "_RED");
            for (int i = data.Count - 1; i >= 0; --i)
            {
                // Variants with global keyword _BLUE disabled are included in the build
                if (!data[i].shaderKeywordSet.IsEnabled(m_GlobalKeywordBlue))
                    continue;  
      
                // Variants with local keyword _RED disabled are included in the build
                if (!data[i].shaderKeywordSet.IsEnabled(localKeywordRed))
                    continue;  
      
                // Any variants that do not meet the criteria above are stripped from the build.
                // In this example, Unity strips variants that have both _BLUE and _RED keywords enabled.
                data.RemoveAt(i);
            }
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

