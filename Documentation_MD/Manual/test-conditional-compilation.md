[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/test-conditional-compilation.html)
  * [中文](/cn/current/Manual/test-conditional-compilation.html)
  * [日本語](/ja/current/Manual/test-conditional-compilation.html)
  * [한국어](/kr/current/Manual/test-conditional-compilation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/test-conditional-compilation.html)
  * [中文](/cn/current/Manual/test-conditional-compilation.html)
  * [日本語](/ja/current/Manual/test-conditional-compilation.html)
  * [한국어](/kr/current/Manual/test-conditional-compilation.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Conditional compilation](conditional-compilation.html)
  * Test conditional compilation

[](custom-scripting-symbols.html)

Custom scripting symbols

[](assembly-definition-files.html)

Organizing scripts into assemblies

# Test conditional compilation

The following example shows how to test your conditionally compiled code. It
also prints a message based on the platform selected for the target build.

## Sample code

    
    
      using UnityEngine;
      using System.Collections;
      public class PlatformDefines : MonoBehaviour {
      void Start () {
    
        #if UNITY_EDITOR
          Debug.Log("Unity Editor");
        #endif
    
        #if UNITY_IOS
          Debug.Log("Unity iOS");
        #endif
    
        #if UNITY_STANDALONE_OSX
            Debug.Log("Standalone OSX");
        #endif
    
        #if UNITY_STANDALONE_WIN
          Debug.Log("Standalone Windows");
        #endif
    
      }          
      } 
    

## Test instructions

  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. Check that the platform you want to test your code on is the Active platform profile. If it isn’t, select your preferred platform and click **Switch Profile**.
  3. Create a [script](creating-scripts.html) and copy and paste the sample code.
  4. In the [Game view](GameView.html) **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar), click the Play button to enter Play
mode. Confirm that the code works by checking for messages relevant to the
platform selected in the Unity console. For example, if you choose iOS, the
messages `Unity Editor` and `Unity iOS` appear in the console.

## Additional resources

  * [Unity scripting symbol reference](scripting-symbol-reference.html)
  * [Custom scripting symbols](custom-scripting-symbols.html)

[](custom-scripting-symbols.html)

Custom scripting symbols

[](assembly-definition-files.html)

Organizing scripts into assemblies

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

