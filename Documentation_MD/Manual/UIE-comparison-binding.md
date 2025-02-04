[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-comparison-binding.html)
  * [中文](/cn/current/Manual/UIE-comparison-binding.html)
  * [日本語](/ja/current/Manual/UIE-comparison-binding.html)
  * [한국어](/kr/current/Manual/UIE-comparison-binding.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-comparison-binding.html)
  * [中文](/cn/current/Manual/UIE-comparison-binding.html)
  * [日本語](/ja/current/Manual/UIE-comparison-binding.html)
  * [한국어](/kr/current/Manual/UIE-comparison-binding.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * Comparison of the binding systems

[](UIE-data-binding.html)

Data binding

[](UIE-runtime-binding.html)

Runtime data binding

# Comparison of the binding systems

The following table compares the SerializedObject data binding and runtime
binding:

**Comparison** | **Runtime binding** | **SerializedObject data binding**  
---|---|---  
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) | Runtime UI, and Editor UI without serialized data. | Editor UI  
Data types | Supports any plain C# `object` as a data source. | Supports only the data types supported by `SerializedProperty`.  
Binding target | Can target multiple properties of the same control. | Targets only the `value` property of a `INotifyValueChanged<T>` control.  
Property paths for a list or an array | Uses the syntax of `Path.To.List[2]`. | Uses the syntax of `Path.To.List.Array.data[2]`.  
Extensibility | You can create your own binding types and attributes. | Not extensible.  
  
## Additional resources

  * [Runtime data binding](UIE-runtime-binding.html)
  * [SerializedObject data binding](UIE-editor-binding.html)

[](UIE-data-binding.html)

Data binding

[](UIE-runtime-binding.html)

Runtime data binding

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

