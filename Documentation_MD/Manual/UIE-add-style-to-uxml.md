[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-add-style-to-uxml.html)
  * [中文](/cn/current/Manual/UIE-add-style-to-uxml.html)
  * [日本語](/ja/current/Manual/UIE-add-style-to-uxml.html)
  * [한국어](/kr/current/Manual/UIE-add-style-to-uxml.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-add-style-to-uxml.html)
  * [中文](/cn/current/Manual/UIE-add-style-to-uxml.html)
  * [日本語](/ja/current/Manual/UIE-add-style-to-uxml.html)
  * [한국어](/kr/current/Manual/UIE-add-style-to-uxml.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI with UXML](UIE-UXML.html)
  * Add styles to UXML

[](UIE-WritingUXMLTemplate.html)

Introduction to UXML

[](UIE-reuse-uxml-files.html)

Reuse UXML files

# Add styles to UXML

In **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit, you can use [USS](UIE-USS.html)
to customize the appearance of **visual elements** A node of a visual tree
that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement). The suggested workflow for USS
is that you visually style an element in UI Builder, extract the style to a
USS file, and then reference it in UXML.

If you style an element in UI Builder, the style is added as an inline style
to the `style` attribute of UXML elements:

    
    
    <ui:UXML ...>
        <ui:VisualElement style="width: 200px; height: 200px; background-color: red;" />
    </ui:UXML>
    

To reference a stylesheet file, add the `<Style>` element under the root
element of a UXML file.

For example, if you have a USS file named `styles.uss` with the following
content:

    
    
    #root {
        width: 200px;
        height: 200px;
        background-color: red;
    }
    

You can reference it like this:

    
    
    <ui:UXML ...>
        <Style src="<path-to-file>/styles.uss" />
        <ui:VisualElement name="root" />
    </ui:UXML>
    

You can use a relative or an absolute path:

  * Absolute paths start from the project’s `Assets` folder and begin with a `/` or `project://database/`. For example, `/Assets/myFolder/myFile.uss` or `project://database/Assets/myFolder/myFile.uss`.
  * Relative paths start from the current file and exclude the `/`. For example, `../myFolder/myFile.uss`.

**Note** : To reference a file from packages, use the absolute path of the
package file that starts from the `Packages` folder. For example,
`/Packages/com.unity.package.name/file-name.uss` or
`project://database/Packages/com.unity.package.name/file-name.uss`. you must
use the format of `com.unity.package.name` rather than `package name` for the
package name.

## Additional resources

  * [Style UI](UIE-USS.html)
  * [Best practices for managing elements](UIE-best-practices-for-managing-elements.html)

[](UIE-WritingUXMLTemplate.html)

Introduction to UXML

[](UIE-reuse-uxml-files.html)

Reuse UXML files

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

