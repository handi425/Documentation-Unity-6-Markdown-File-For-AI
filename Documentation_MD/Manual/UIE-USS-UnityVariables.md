[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-USS-UnityVariables.html)
  * [中文](/cn/current/Manual/UIE-USS-UnityVariables.html)
  * [日本語](/ja/current/Manual/UIE-USS-UnityVariables.html)
  * [한국어](/kr/current/Manual/UIE-USS-UnityVariables.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-USS-UnityVariables.html)
  * [中文](/cn/current/Manual/UIE-USS-UnityVariables.html)
  * [日本語](/ja/current/Manual/UIE-USS-UnityVariables.html)
  * [한국어](/kr/current/Manual/UIE-USS-UnityVariables.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Style UI](UIE-USS.html)
  * [USS custom properties (variables)](UIE-USS-variables.html)
  * Introduction to USS built-in variables

[](UIE-USS-CustomProperties.html)

Create USS variables

[](UIE-uss-built-in-variable-reference.html)

USS built-in variable references

# Introduction to USS built-in variables

USS built-in [variables](UIE-USS-CustomProperties.html) specify default values
for Editor and runtime **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI). You can use these variables in your own
USS to match your custom interfaces with Unity style.

The name of each built-in variable indicates how and where the variable is
used. A variable name consists of one or more parts, separated by hyphens.
Each part consists of one or more words separated by underscores.

`--unity-{group}-{role_and_control}-{sub_element}-{pseudo_state_sequence}`

Each part of the name shows the types of USS rules that use the variable.

  * **Group**: The kind of data the variable represents.
  * **Role/Control**: A conceptual grouping for the elements the variable affects.
  * **Sub-Element**: An element or control the variable affects.
  * **Pseudo States**: Lists the states Unity uses the variable for.

For example, the following variable name:

`--unity-colors-button-text-hover`

Provides the following information about how Unity uses the variable:

| **Value** | **Meaning**  
---|---|---  
**Group** | `colors` | Represents color data.  
**Role/Control** | `button` | Affects buttons.  
**Sub-Element** | `text` | Affects text. Its `group` is `colors`, so it affects text color.  
**Pseudo-States** | `hover` | Applies to elements when the mouse pointer hovers over them.  
  
This USS built-in variable changes the color of button text when a user hovers
over the button.

## Group

The group specifies what kind of data the variable represents. Each group has
several possible sub-elements.

The variable names have the following groups:

**Group** | **Used for**  
---|---  
`colors` | Color properties, such as `background-color` and `border-color`  
`metrics` | Properties that control dimensions and shapes. For example, `border-radius`, `border-width`, `margin`, and `padding`  
`icons` | Standard Unity icon images  
  
## Role and Control

Roles and controls are two ways of grouping elements conceptually.

  * **Role** refers to a group of elements that have the same purpose, regardless of what type each element is. For example, the `error` role includes all elements that display error messages to users.
  * **Control** refers to a group of elements of the same type, regardless of what they do. For example, `buttons` includes all buttons in the Editor.

Each variable has either a role or a control.

The variable names have the following roles and controls:

**Roles**

**Role** | **Description**  
---|---  
`default` | Default style settings such as text color, background, and margin.  
`alternated_rows` | Elements that display tabular data with alternating row colors. For example, list items in a list view.  
`error` | Elements that communicate error states to users.  
`highlight` | Highlighted parts of the UI. For example, text selections, or selected items in tree views.  
`link` | Parts of the UI (typically text) that are clickable links. This is the un-clicked state.  
`play_mode` | Elements displayed when the Editor is in Play mode.  
`visited_link` | Parts of the UI, typically text, that are clickable links that a user has already clicked.  
`warning` | Elements that communicate a warning message to users.  
  
**Controls**

**Control** | **Description**  
---|---  
`app_toolbar` | The main Unity **toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar)  
`app_toolbar_button` | Buttons in the main Unity toolbar  
`box` | Boxes used to group elements in the Editor UI  
`button` | Buttons in the UI, except for toolbars  
`dropdown` | Dropdown lists or menus  
`helpbox` | Boxes used to display help information  
`input_field` | Fields used to input text or numeric values  
`label` | Text labels in the Editor UI  
`object_field` | Fields used for object values. For example, property values for a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or Asset.  
`popup` | Popup menu and other popup controls  
`preview` | Views used to display previews. For example, of Assets such as meshes and textures.  
`scrollbar_groove` | The background element of a scrollbar in which users drag the scrollbar thumb  
`scrollbar_thumb` | The draggable handle element in a scrollbar  
`slider_groove` | The background element of a slider in which users drag the slider thumb  
`slider_thumb` | The draggable handle element in a slider  
`slider_thumb_halo` | An overlay displayed around the slider thumb when the user drags it  
`tab` | Tab items in tab controls  
`toolbar` | Any Editor toolbar except for the main Unity toolbar (`app_toolbar`)  
`toolbar_button` | Buttons in an Editor toolbar  
`window` | Editor windows  
  
## Sub-Element

The sub-element is the part of an element that the variable affects. Together
with a variable’s `group`, the sub-element shows what kind of data the
variable represents.

For example, when you see a variable name with the `colors` group and the
`text` sub-element, it means Unity uses the variable in styles that affect
text color.

The variable names have the following sub-elements:

**Group** | **Sub-element** | **Description**  
---|---|---  
`colors`  
| `background` | An element’s background color  
| `border` | An element’s outer border color  
| `border_accent` | An element’s inner border color. For example, **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) windows have a two-tone border  
| `text` | Text color for elements that display text  
`metrics`  
| `margin_{left, top, right, bottom}` | An element’s margin values  
| `padding_{left, top, right, bottom}` | An element’s padding values  
| `border_{left, top, right, bottom}_width` | An element’s border width values  
| `border_{left_top, left_bottom, right_top, right_bottom}_radius` | An element’s border radius values values  
| `width, height` | An element’s width and height values  
  
## Pseudo-States

The pseudo-state sequence is a list of UI states that Unity uses a variable
for.

For example, when you see a variable name with the `hover` pseudo state, it
means Unity uses the variable in styles that affect elements when a user
hovers the pointer over them.

For example: `--unity-colors-toolbar_button-text-hover`.

A variable name can have more than one pseudo-state. Multiple pseudo states
appear in alphabetical order, separated by underscores `_`.

For example: `--unity-colors-toolbar_button-text-focus_selected`.

Unity variable names can have any combination of the following pseudo-states:

**Pseudo-state** | **Description**  
---|---  
(none) | Normal state  
`checked` | A checkbox-type control is checked  
`disabled` | A control is disabled  
`focus` | A control has focus  
`hover` | A user hovers over a control  
`inactive` | A control doesn’t have focus  
`pressed` | A control is pressed  
`selected` | A control is selected  
  
## Additional resources

  * [Create USS variables](UIE-USS-CustomProperties.html)
  * [USS built-in variable reference](UIE-uss-built-in-variable-reference.html)

[](UIE-USS-CustomProperties.html)

Create USS variables

[](UIE-uss-built-in-variable-reference.html)

USS built-in variable references

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

