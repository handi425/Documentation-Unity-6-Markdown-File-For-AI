[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-runtime-binding-logging-levels.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-logging-levels.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-logging-levels.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-logging-levels.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-runtime-binding-logging-levels.html)
  * [中文](/cn/current/Manual/UIE-runtime-binding-logging-levels.html)
  * [日本語](/ja/current/Manual/UIE-runtime-binding-logging-levels.html)
  * [한국어](/kr/current/Manual/UIE-runtime-binding-logging-levels.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Data binding](UIE-data-binding.html)
  * [Runtime data binding](UIE-runtime-binding.html)
  * Define logging levels

[](UIE-runtime-binding-data-type-conversion.html)

Convert data types

[](UIE-runtime-binding-custom-types.html)

Create custom binding types

# Define logging levels

During the update of the binding, errors might occur where binding objects try
to access invalid properties, encounter `null` values along a property path,
or encounter missing type converters. By default, the binding system logs all
errors to the Console, which can impact performance.

To control the console output, you can define logging levels for the binding
system. The following are the available logging levels:

  * **BindingLogLevel.All** Errors are consistently logged to the console.
  * **BindingLogLevel.Once** : Errors are logged to the console only the first time they occur.
  * **BindingLogLevel.None** : Error logging is disabled.

You can set the global and per-panel configurations to customize logging
behavior.

The following example sets the global log level of all panels or windows.

    
    
    Binding.SetGlobalLogLevel(BindingLogLevel.Once);
    

The following example sets the log level per panel:

    
    
    Binding.SetPanelLogLevel(myElement.panel, BindingLogLevel.None);
    

**Note:** The per-panel or the per-window logging level settings override the
global logging level settings.

## Additional resources

  * [Runtime data binding](UIE-runtime-binding.html)
  * [Create runtime data binding](UIE-runtime-binding-types.html)
  * [Define a data source](UIE-runtime-binding-define-data-source.html)
  * [Define binding modes and update triggers](UIE-runtime-binding-mode-update.html)
  * [Convert data types](UIE-runtime-binding-data-type-conversion.html)

[](UIE-runtime-binding-data-type-conversion.html)

Convert data types

[](UIE-runtime-binding-custom-types.html)

Create custom binding types

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

