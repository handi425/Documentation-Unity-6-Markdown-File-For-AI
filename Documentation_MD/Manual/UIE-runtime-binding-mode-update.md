[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-runtime-binding-mode-update.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-mode-update.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-mode-update.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-mode-update.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-runtime-binding-mode-update.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-mode-update.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-mode-update.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-mode-update.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [Runtime data binding](UIE-runtime-binding.html)
  * Define binding mode and update trigger

[](UIE-runtime-binding-define-data-source.html)

Define a data source for runtime binding

[](UIE-runtime-binding-data-type-conversion.html)

Convert data types

# Define binding mode and update trigger

To define how changes are replicated between the data source and the
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), you can set the binding mode and update
triggers for a binding object. You can set the binding mode and update
triggers in UI Builder, UXML, or C#.

## Define binding modes

[Binding modes](../ScriptReference/UIElements.BindingMode.html) configure how
changes are replicated between the data source and the UI. The following
binding modes are available:

  * **TwoWay** : Changes are replicated from the data source to the UI and from the UI to the data source. This is the default binding mode.
  * **ToTarget** : Changes are replicated from the data source to the UI only.
  * **ToSource** : Changes are replicated from the UI to the data source only.
  * **ToTargetOnce** : Changes are replicated from the data source to the UI only once, unless it’s [marked as dirty](../ScriptReference/UIElements.Binding.MarkDirty.html).

**Tip** : Ensure that you set the appropriate binding mode based on your
needs. For example, to prevent changes in the UI from being reflected in the
source or if the UI is read-only, set the `bindingMode` to
`BindingMode.ToTarget`.

## Define update triggers

You can update binding objects on every frame or when a change occurs in the
data source. The following update triggers are available:

  * Every frame
  * On change detection or every frame if change detection is impossible. Refer to [Define data sources](UIE-runtime-binding-define-data-source.html) for more details.
  * When explicitly marked as [`dirty`](../ScriptReference/UIElements.Binding-isDirty.html)

To define update triggers, use the following properties:

  * [`MarkDirty`](../ScriptReference/UIElements.Binding.MarkDirty.html): Sets the binding object as [`dirty`](../ScriptReference/UIElements.Binding-isDirty.html), so that it gets updated during the next cycle.
  * [`updateTrigger`](../ScriptReference/UIElements.Binding-updateTrigger.html): Updates a binding object on every frame, regardless of the data source version.

**Note** : Don’t keep binding types per-element state. You can use a binding
instance across multiple elements and properties simultaneously. During
updates and callbacks, the binding system passes in a context object that
contains the target element, binding ID, and relevant data. You can use this
context object to store the per-element state.

## Additional resources

  * [Runtime data binding](UIE-runtime-binding.html)
  * [Create runtime data binding](UIE-runtime-binding-types.html)
  * [Define a data source](UIE-runtime-binding-define-data-source.html)
  * [Convert data types](UIE-runtime-binding-data-type-conversion.html)
  * [Define logging levels](UIE-runtime-binding-logging-levels.html)
  * [Create custom binding types](UIE-runtime-binding-custom-types.html)

[](UIE-runtime-binding-define-data-source.html)

Define a data source for runtime binding

[](UIE-runtime-binding-data-type-conversion.html)

Convert data types

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

