[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-CustomProperties.html)
  * [中文](/cn/current/Manual/UIE-USS-CustomProperties.html)
  * [日本語](/ja/current/Manual/UIE-USS-CustomProperties.html)
  * [한국어](/kr/current/Manual/UIE-USS-CustomProperties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-CustomProperties.html)
  * [中文](/cn/current/Manual/UIE-USS-CustomProperties.html)
  * [日本語](/ja/current/Manual/UIE-USS-CustomProperties.html)
  * [한국어](/kr/current/Manual/UIE-USS-CustomProperties.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS custom properties (variables)](UIE-USS-variables.html)
  * Create USS variables

[](UIE-USS-variables.html)

USS custom properties (variables)

[](UIE-USS-UnityVariables.html)

Introduction to USS built-in variables

# Create USS variables

You can create a USS variable and use it in other USS properties. When you
update a USS variable, all of the USS properties that use that variable
update. You can also specify default values for USS variables.

## Create and use USS variables

To create a USS variable, prefix its name with a double-hyphen (`--`).

    
    
    --color-1: red;
    

To use a USS variable value in another USS rule, use the `var()` function to
call it.

    
    
    var(--color-1);
    

When you update a variable, it updates all the USS properties that use it.

For example, the following USS snippet defines one style rule that declares
two color variables, and two style rules that use those variables.

    
    
    :root {
      --color-1: blue;
      --color-2: yellow;
    }
    
    .paragraph-regular {
      color: var(--color-1);
      background: var(--color-2);
      padding: 2px;
      }
    
    .paragraph-reverse {
      color: var(--color-2);
      background: var(--color-1);
      padding: 2px;
      }
    

To update the color scheme, you can change the two variable values instead of
the four color values.

Variables make it easier to manage styles for complex **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI), where multiple rules, sometimes in
different style sheets, use the same values.

## Specify default values for USS variables

The `var()` function accepts an optional default value. The UI system uses the
default value when it cannot resolve the variable. For example, if you remove
a variable from a style sheet but forget to remove a reference to it.

To specify a default value for a variable, add it after the variable value,
separated by a comma `,`.

The following USS snippet calls the `--color-1` variable. If the UI system
can’t resolve the variable, it uses the hex value for red (`#FF0000`).

    
    
    var(--color-1, #FF0000);
    

## Differences from CSS variables

Variables work mostly the same way in USS as they do in CSS. For detailed
information about CSS variables, see the [MDN
documentation](https://developer.mozilla.org/en-
US/docs/Web/CSS/Using_CSS_custom_properties). However, USS doesn’t support
some of the functionalites of CSS:

  * USS doesn’t support the `var()` function inside of other functions, such as shown below:

    
    
      background-color: rgb(var(--red), 0, 0);
    

  * USS doesn’t support mathematical operations on variables.

## Additional resources

  * [Introduction to USS built-in variables](UIE-USS-UnityVariables.html)
  * [USS built-in variable reference](UIE-uss-built-in-variable-reference.html)

[](UIE-USS-variables.html)

USS custom properties (variables)

[](UIE-USS-UnityVariables.html)

Introduction to USS built-in variables

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

