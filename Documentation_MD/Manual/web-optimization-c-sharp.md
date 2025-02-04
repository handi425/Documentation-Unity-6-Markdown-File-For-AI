[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/web-optimization-c-sharp.html)
  * [中文](/cn/current/Manual/web-optimization-c-sharp.html)
  * [日本語](/ja/current/Manual/web-optimization-c-sharp.html)
  * [한국어](/kr/current/Manual/web-optimization-c-sharp.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/web-optimization-c-sharp.html)
  * [中文](/cn/current/Manual/web-optimization-c-sharp.html)
  * [日本語](/ja/current/Manual/web-optimization-c-sharp.html)
  * [한국어](/kr/current/Manual/web-optimization-c-sharp.html)

  * [Platform development ](PlatformSpecific.html)
  * [Web](webgl.html)
  * [Build and distribute a Web application](webgl-building-distribution.html)
  * [Optimize your Web build](web-optimization.html)
  * Use C# code to enable optimization settings

[](web-optimization-quality.html)

Recommended Quality settings to optimize your Web build

[](web-optimization-remove-resources.html)

Remove unused resources from your Web build

# Use C# code to enable optimization settings

You can use code to enable some optimizations recommended in [Optimize your
Web build](web-optimization.html). If you use code to configure these settings
it can save you time having to manually set each of them individually.

**Note** : This script only works in the Unity Editor, not in builds.

## Create a C# script to optimize your Web build

To use code to enable most of these optimizations at once in your Unity
**project settings** A broad collection of settings which allow you to
configure how Physics, Audio, Networking, Graphics, Input and many other areas
of your project behave. [More info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings):

  1. Create an `Assets/Editor` folder if you don’t already have one.

  2. Create an empty C# script in the `Editor` folder.

  3. Paste the following code into the script:
    
        using UnityEditor;
    using UnityEditor.Build;
    using UnityEngine;
    
    public class WebOptimizer
    {
        [MenuItem("Example/Optimize")]
        public static void Optimize()
        {
            var namedBuildTarget = NamedBuildTarget.WebGL;
            var buildOptions = BuildOptions.CompressWithLz4HC;
    
            // Set IL2CPP code generation to Optimize Size 
            PlayerSettings.SetIl2CppCodeGeneration(namedBuildTarget,         
                                            Il2CppCodeGeneration.OptimizeSize);
    
            // Set the Managed Stripping Level to High
            PlayerSettings.SetManagedStrippingLevel(namedBuildTarget,     
                                                ManagedStrippingLevel.High);  
    
            // Strip unused mesh components           
            PlayerSettings.stripUnusedMeshComponents = true;
    
            // Enable data caching
            PlayerSettings.WebGL.dataCaching = true;
    
            // Set the compression format to Brotli
            PlayerSettings.WebGL.compressionFormat = WebGLCompressionFormat.Brotli;
    
            // Deactivate exceptions
            PlayerSettings.WebGL.exceptionSupport = WebGLExceptionSupport.None;
    
            // Deactivate debug symbols
            PlayerSettings.WebGL.debugSymbolMode = WebGLDebugSymbolMode.Off;
    
            //Enable WebAssembly 2023 features
            PlayerSettings.WebGL.wasm2023 = true;           
    
            // Set Platform Settings to optimize for disk size (LTO)
            UnityEditor.WebGL.UserBuildSettings.codeOptimization = UnityEditor.WebGL.WasmCodeOptimization.DiskSizeLTO;
        }
    }
    

  4. Change the script to suit your project.

  5. From the toolbar, select **Example** > **Optimize** to run the script. Your settings update.

To change the settings for Asset Import Overrides, refer to [Build profile
reference](build-profiles-reference.html#AssetImportOverride).

## Additional resources

  * [Optimize your Web build](web-optimization.html)

  * [Recommended Graphics settings to optimize your Web build](web-optimization-graphics.html)

  * [Recommended Player settings to optimize your Web build](web-optimization-player.html)

  * [Recommended Quality settings to optimize your Web build](web-optimization-quality.html)

  * [Remove unused resources from your Web build](web-optimization-remove-resources.html)

  * [Optimize Web platform for mobile](web-optimization-mobile.html)

[](web-optimization-quality.html)

Recommended Quality settings to optimize your Web build

[](web-optimization-remove-resources.html)

Remove unused resources from your Web build

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

