[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-data-binding.html)
  * [中文](/cn/current/Manual/UIE-data-binding.html)
  * [日本語](/ja/current/Manual/UIE-data-binding.html)
  * [한국어](/kr/current/Manual/UIE-data-binding.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-data-binding.html)
  * [中文](/cn/current/Manual/UIE-data-binding.html)
  * [日本語](/ja/current/Manual/UIE-data-binding.html)
  * [한국어](/kr/current/Manual/UIE-data-binding.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * Data binding

[](UIE-parallel-tessellation.html)

Parallel tessellation

[](UIE-comparison-binding.html)

Comparison of the binding systems

# Data binding

Data binding synchronizes properties of non-UI objects, such as a string
property on a
[MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html),
with properties of **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) objects, such as the value property of a
TextField. A binding refers to the link between the property and the visual
control that modifies it. Use bindings to synchronize values between a
property and a specific **visual element** A node of a visual tree that
instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement), so you don’t need to write
[event handlers](UIE-Events-Handling.html) when the value changes in the UI.

UI Toolkit supports two types of data binding systems that you can use to
create bindings for the Editor UI and the runtime UI.

**Topic** | **Description**  
---|---  
[Comparison of the binding systems](UIE-comparison-binding.html) | Compares the runtime binding and the SerializedObject data binding.  
[Runtime data binding](UIE-runtime-binding.html) | Binds the properties of any plain C# `object` to the properties of a UI control. You can use this type of data binding in the runtime UI. You can also use it in the Editor UI as long as it’s not for serialized data.  
[SerializedObject data binding](UIE-editor-binding.html) | Binds the properties of a `SerializedObject` to the properties of a UI control. You can use this type of data binding only in the Editor UI.  
  
## Additional resources

  * [Mini-tutorial: Data binding with UI Builder and C# in 5 minutes](https://discussions.unity.com/t/mini-tutorial-data-binding-with-ui-builder-and-c-in-5-minutes/1544817)
  * [Support for Editor UI](UIE-support-for-editor-ui.html)
  * [Support for runtime](UIE-support-for-runtime-ui.html)

[](UIE-parallel-tessellation.html)

Parallel tessellation

[](UIE-comparison-binding.html)

Comparison of the binding systems

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

