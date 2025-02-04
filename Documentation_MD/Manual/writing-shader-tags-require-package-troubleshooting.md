[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [中文](/cn/current/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-require-package-troubleshooting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [中文](/cn/current/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [日本語](/ja/current/Manual/writing-shader-tags-require-package-troubleshooting.html)
  * [한국어](/kr/current/Manual/writing-shader-tags-require-package-troubleshooting.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Writing custom shaders](writing-custom-shaders.html)
  * [Writing shaders in code](shader-writing.html)
  * [Configure when and if Unity uses a shader](writing-shader-tags.html)
  * Troubleshooting package requirement definitions

[](writing-shader-tags-get-tag-value.html)

Get tag values in a script

[](class-ComputeShader.html)

Compute shaders

# Troubleshooting package requirement definitions

If you define package requirements that can never be satisfied, the **shader**
A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) import process fails with an error.
This section provides examples of the most common invalid package requirement
definitions.

## Malformed versions or empty package name

    
    
    PackageRequirements {
      "com.some.package.x": "[10.2.1,9.0]"        // Error, empty version range
      "com.some.package.y": "[10.2.1.9,11.0]"     // Error, incorrect version format
      "com.some.package.z": "[2.3,3.5],[3.0,4.0]" // Error, ranges intersect
      "com.some.package.z" : "[10.2.1,11.0]"      // Error, extra whitespace after the package name
      "" : "[2.3.4,3.4.5]"                        // Error, no package name provided
    }
    

## Multiple dependencies on the same package

    
    
    PackageRequirements {
      "com.some.package.x": "[10.2.1,11.0]"
      "com.some.package.x": "[11.2.1,12.0]" // Error, dependency on "com.some.package.x" declared twice
      "unity" : "2021.2"
      "unity" : "2021.3" // Error, dependency on Unity version declared twice
    }
    

## Conflicting dependency declarations

    
    
    PackageRequirements {
      "com.some.package.x": "unity=[2021.2.1,2021.3.3]"
      "unity" : "2021.2"    // Error: Unity version requirement cannot be declared on a package and on its own simultaneously
    }
    

## Conflicting dependency declarations between SubShaders and Passes

    
    
    SubShader {
      PackageRequirements {
        "com.some.package.x": "[2.3.4,3.4.5]"
        "com.some.package.z": "[1.1,3.2]"
        "unity": "2021.2"
      }
      Pass {
        PackageRequirements {
          "com.some.package.y": "[1.2.2,2.5]"               // Fine, SubShader doesn’t declare a dependency on "com.some.package.y"
          "com.some.package.z": "[2.0,3.1]"                 // Fine, SubShader dependency intersects the provided version range
          "com.some.package.x": "[1.1.1, 2.2.2]"            // Error, SubShader version range for "com.some.package.x" does not intersect the provided range
          "com.some.package.w": "unity=[2021.2.1,2021.2.5]" // Fine, SubShader dependency intersects the provided version range
          "com.some.package.u": "unity=[2020.2.1,2020.2.5]" // Error, SubShader Unity version range does not intersect the provided range
        }
      }
    }
    

## Additional resources

  * [Set a shader to require a package](writing-shader-tags-require-package.html)

[](writing-shader-tags-get-tag-value.html)

Get tag values in a script

[](class-ComputeShader.html)

Compute shaders

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

