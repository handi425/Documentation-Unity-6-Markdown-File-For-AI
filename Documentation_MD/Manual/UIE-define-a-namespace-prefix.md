[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-define-a-namespace-prefix.html)
  * [中文](/cn/current/Manual/UIE-define-a-namespace-prefix.html)
  * [日本語](/ja/current/Manual/UIE-define-a-namespace-prefix.html)
  * [한국어](/kr/current/Manual/UIE-define-a-namespace-prefix.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-define-a-namespace-prefix.html)
  * [中文](/cn/current/Manual/UIE-define-a-namespace-prefix.html)
  * [日本語](/ja/current/Manual/UIE-define-a-namespace-prefix.html)
  * [한국어](/kr/current/Manual/UIE-define-a-namespace-prefix.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Custom controls](UIE-custom-controls.html)
  * Define a namespace prefix

[](UIE-bind-custom-control-to-data.html)

Bind custom controls to data

[](UIE-troubleshooting-custom-control-library-compilation.html)

Troubleshooting custom control library compilation

# Define a namespace prefix

After you have defined a custom control element, you can use it in your UXML
files. To categorize elements, create the class in a namespace. When you
define a new namespace, you can define a prefix for the namespace. You must
define namespace prefixes as attributes of the root `<UXML>` element and
replace the full namespace name when scoping elements.

To define a namespace prefix, add a `UxmlNamespacePrefix` attribute to your
assembly for each namespace prefix. For example:

    
    
    [assembly: UxmlNamespacePrefix("My.First.Namespace", "first")]
    [assembly: UxmlNamespacePrefix("My.Second.Namespace", "second")]
    

You can do this at the root level (outside any namespace) of any C# file of
the assembly.

The schema generation system does the following:

  * Checks for these attributes and uses them to generate the schema.
  * Adds the namespace prefix definition as an attribute of the `<UXML>` element in newly created UXML files.
  * Includes the schema file location for the namespace in its `xsi:schemaLocation` attribute.

To ensure that your text editor recognizes the new element, select **Assets**
> **Update UXML Schema** to update the schema definition.

To create a new UXML document with the prefix, select **Assets** > **Create**
> **UI Toolkit** > **UI Document**.

## Additional resources

  * [Create custom controls](UIE-create-custom-controls.html)

[](UIE-bind-custom-control-to-data.html)

Bind custom controls to data

[](UIE-troubleshooting-custom-control-library-compilation.html)

Troubleshooting custom control library compilation

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

