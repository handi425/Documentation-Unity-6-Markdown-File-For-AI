[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/managed-code-stripping-configure.html)
  * [中文](/cn/current/Manual/managed-code-stripping-configure.html)
  * [日本語](/ja/current/Manual/managed-code-stripping-configure.html)
  * [한국어](/kr/current/Manual/managed-code-stripping-configure.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/managed-code-stripping-configure.html)
  * [中文](/cn/current/Manual/managed-code-stripping-configure.html)
  * [日本語](/ja/current/Manual/managed-code-stripping-configure.html)
  * [한국어](/kr/current/Manual/managed-code-stripping-configure.html)

  * [Scripting](scripting.html)
  * [Compilation and code reload ](compilation-and-code-reload.html)
  * [Script compilation](script-compilation.html)
  * [Managed code stripping](managed-code-stripping.html)
  * Configure managed code stripping

[](unity-linker.html)

Managed code stripping and the Unity linker

[](managed-code-stripping-preserving.html)

Preserving code using annotations

# Configure managed code stripping

The **Managed Stripping Level** property determines which [rules](managed-
code-stripping-marking-rules.html) the Unity linker follows when it analyzes
and strips your application’s code. Increasing the managed stripping level
expands the scope of the linker’s search for unused code but also increases
build time.

To change the **Managed Stripping Level** property:

  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , navigate to the Optimization heading.
  3. Set the **Managed Stripping Level** property to the desired value.

**Property** | **Function**  
---|---  
**Disabled** | Unity doesn’t remove any code.  
  
This setting is only available for the [Mono scripting backend](scripting-
backends-mono.html) and is the default setting in that case.  
**Minimal** | Unity searches only the `UnityEngine` and the .NET class libraries for unused code. Unity doesn’t remove any user-written code. This setting is the least likely to cause unexpected runtime behavior.  
  
This setting is useful for projects where usability is of higher priority than
build size. This is the default setting if you use the [IL2CPP scripting
backend](scripting-backends-il2cpp.html).  
**Low** | Unity searches for unused code in all `UnityEngine` and .NET class libraries. It also searches user-written assemblies, but only if none of their types are referenced in scenes included in the Player build. This setting applies a set of rules that removes some unused code but minimizes the likelihood of unintended consequences, such as changes in behavior of runtime code that uses reflection.  
  
**Note** : The **Low** managed stripping level is marked for future
deprecation and using it is not recommended. Use **Minimal** or **Medium**
instead.  
**Medium** | Unity partially searches all assemblies to find unused code. This setting applies a set of rules that strips more types of code patterns to reduce the build size. Although Unity doesn’t strip all possible unused code, this setting does increase the risk of undesirable or unexpected behavior changes.  
**High** | Unity performs an extensive search of all assemblies to find unused code. At this setting, Unity prioritizes size reduction more than code stability and removes as much code as possible.  
  
This search can take much longer than for lower stripping levels. Use this
setting only for projects where a compact build size is extremely important.
Test your application thoroughly and make careful use of `[Preserve]`
attributes and `link.xml` files to ensure that the Unity linker doesn’t strip
vital code.  
  
## Additional resources

  * [Managed code stripping and the Unity linker](unity-linker.html)
  * [Preserving code using annotations](managed-code-stripping-preserving.html)
  * [Link XML formatting reference](managed-code-stripping-xml-formatting.html)
  * [Unity linker marking rules reference](managed-code-stripping-marking-rules.html)
  * [IUnityLinkerProcessor.GenerateAdditionalLinkXmlFile](../ScriptReference/Build.IUnityLinkerProcessor.GenerateAdditionalLinkXmlFile.html)

[](unity-linker.html)

Managed code stripping and the Unity linker

[](managed-code-stripping-preserving.html)

Preserving code using annotations

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

