[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-WritingUXMLTemplate.html)
  * [中文](/cn/current/Manual/UIE-WritingUXMLTemplate.html)
  * [日本語](/ja/current/Manual/UIE-WritingUXMLTemplate.html)
  * [한국어](/kr/current/Manual/UIE-WritingUXMLTemplate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-WritingUXMLTemplate.html)
  * [中文](/cn/current/Manual/UIE-WritingUXMLTemplate.html)
  * [日本語](/ja/current/Manual/UIE-WritingUXMLTemplate.html)
  * [한국어](/kr/current/Manual/UIE-WritingUXMLTemplate.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI with UXML](UIE-UXML.html)
  * Introduction to UXML

[](UIE-UXML.html)

Structure UI with UXML

[](UIE-add-style-to-uxml.html)

Add styles to UXML

# Introduction to UXML

The UXML format is inspired by [HTML](https://developer.mozilla.org/en-
US/docs/Web/HTML), [XAML](https://docs.microsoft.com/en-
us/dotnet/desktop/wpf/xaml/?view=netdesktop-5.0), and
[XML](https://developer.mozilla.org/en-US/docs/Web/XML/XML_introduction). If
you’ve worked with these formats before, you’ll find similarities in UXML.
However, the UXML format includes small differences to provide an efficient
way to work with Unity. This page introduces the format of UXML by an example.

The following is an example UXML file. It contains several built-in
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) controls that prompt the user to make a
choice:

    
    
    <?xml version="1.0" encoding="utf-8"?>
    <UXML ...>
        <Box>
            <Toggle name="boots" label="Boots" value="false" />
            <Toggle name="helmet" label="Helmet" value="false" />
            <Toggle name="cloak" label="Cloak of invisibility" value="false"/>
        </Box>
        <Box>
            <Button name="cancel" text="Cancel" />
            <Button name="ok" text="OK" />
        </Box>
    </UXML>
    

## UXML declaration

The first line of code in the above UXML example is the UXML declaration. The
declaration is optional. If you do include the UXML declaration, you must put
it on the first line. A UXML declaration requires a `version`. The `encoding`
attribute is optional in a UXML declaration. If you include the `encoding`
attribute, you must declare the character encoding of the file.

## Document root

The next line defines the document root, `<UXML>`. The `<UXML>` element
includes attributes for the namespace prefix definitions and the location of
schema definition files. You can specify these attributes in any order.

## Namespace

In UI Toolkit, each element is defined in either the `UnityEngine.UIElements`
or the `UnityEditor.UIElements` namespace:

  * The `UnityEngine.UIElements` namespace contains elements that are defined as part of the Unity runtime.
  * The `UnityEditor.UIElements` namespace contains elements that are available in the Unity Editor. To fully specify an element, you must prefix it with its namespace.

For example, if you want to use the `Button` element in your UXML template,
you must specify `<UnityEngine.UIElements:Button />`.

To make specifying namespaces easier, you can define a namespace prefix. For
example, `xmlns:engine="UnityEngine.UIElements"` defines the `engine` prefix
as `UnityEngine.UIElements`. Once you define a namespace prefix, you can use
it to specify namespaces. For example, `<engine:Button />` is equivalent to
`<UnityEngine.UIElements:Button />`

You can also define a default namespace by excluding a prefix. For example,
`xmlns="UnityEngine.UIElements"` defines `UnityEngine.UIElements` as the
default namespace. This means that specifying, for example, `<Button />` is
equivalent to `<UnityEngine.UIElements:Button />`

To create a UXML file with automatically defined namespaces, select **Asset**
> **Create** > **UI Toolkit** > **UI Document**.

**Note** : If you define your own elements, don’t define the custom control
class in the `UnityEngine.UIElements` or `UnityEditor.UIElements` namespace.
Otherwise, UI Builder will hide your custom controls.

## Schema definition

The schema definition validates your UXML files. It specifies which attributes
and child elements each UXML element can contain.

In a UXML file, the `xsi:noNamespaceSchemaLocation` or the
`xsi:schemaLocation` attributes of the `<UXML>` root element specify the
location of the schema definition files.

To create a UXML file with the latest schema definition, select **Assets** >
**Create** > **UI Toolkit** > **UI Document**. This creates a file with the
`xsi:noNamespaceSchemaLocation` attribute for the root element.

**Note** : If your text editor doesn’t recognize the
`xsi:noNamespaceSchemaLocation` attribute, use the `xsi:schemaLocation`
attribute instead.

To force an update of the UXML schema definition, select **Assets** > **Update
UXML Schema**.

## UXML elements

The definition of the UI is within the `<UXML>` root. The UI definition is a
series of nested UXML elements, each representing a visual element.

The element name corresponds to the C# class name of the element to
instantiate. Most elements have attributes and their values are mapped to the
corresponding class properties in C#. Each element has its own set of
attributes in addition to the inherited attributes of its parent class.
`VisualElement` is the base class for all elements and it provides the
following attributes for all elements:

  * `name`: An identifier for the element. The name should be unique.
  * `picking-mode`: Set to either `Position` to respond to mouse events or `Ignore` to ignore mouse events.
  * `focus-index`: (**OBSOLETE**) Use `tabIndex` and `focusable`.
  * `tabindex`: An integer that defines the tabbing position of the current element.
  * `focusable`: A Boolean that indicates whether the element is focusable.
  * `class`: A space-separated list of identifiers that characterize the element. Use classes to assign visual styles to elements. You can also use classes to select a set of elements in UQuery.
  * `tooltip`: A string that displays as a tooltip when the mouse hovers over the element.
  * `view-data-key` : A string that defines the key used for serialization of the element.

## Additional resources

  * [Add styles to UXML](UIE-add-style-to-uxml.html)
  * [Reuse UXML files](UIE-reuse-uxml-files.html)
  * [Reference other files from UXML](UIE-reference-other-files-from-uxml.html)
  * [UXML elements Reference](UIE-ElementRef.html)

[](UIE-UXML.html)

Structure UI with UXML

[](UIE-add-style-to-uxml.html)

Add styles to UXML

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

