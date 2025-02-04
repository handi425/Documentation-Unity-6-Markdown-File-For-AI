[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/features/rendering-debugger-add-controls.html)
  * [中文](/cn/current/Manual/urp/features/rendering-debugger-add-controls.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-debugger-add-controls.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-debugger-add-controls.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/features/rendering-debugger-add-controls.html)
  * [中文](/cn/current/Manual/urp/features/rendering-debugger-add-controls.html)
  * [日本語](/ja/current/Manual/urp/features/rendering-debugger-add-controls.html)
  * [한국어](/kr/current/Manual/urp/features/rendering-debugger-add-controls.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Graphics performance and profiling](../../graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](../../graphics-performance-and-profiling-in-urp.html)
  * [Rendering Debugger in URP](../../urp/features/rendering-debugger.html)
  * Add controls to the Rendering Debugger in URP

[](../../urp/features/rendering-debugger-use.html)

Enable the Rendering Debugger in URP

[](../../urp/features/rendering-debugger-reference.html)

Rendering Debugger window reference for URP

# Add controls to the Rendering Debugger in URP

You can customise the [Rendering Debugger window](rendering-debugger.html)
with your own controls and **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More
info](../../creating-scripts.html)  
See in [Glossary](../../Glossary.html#Scripts), to visualize your project’s
lighting, rendering or Material properties.

The **Rendering Debugger** window contains multiple tabs (‘panels’). When you
select a panel, the window displays one or more controls (‘widgets’).

To create a widget and add it to a new panel, do the following:

  1. Create a script that uses `using UnityEngine.Rendering;` to include the `UnityEngine.Rendering` namespace.
  2. Create a widget by creating an instance of a child class of [DebugUI.Widget](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@15.0/api/UnityEngine.Rendering.DebugUI.Widget.html), for example `DebugUI.Button`.
  3. In the widget, implement the `onValueChanged` callback, which Unity calls when you change the value in the widget.
  4. Create a panel using [DebugUI.instance.GetPanel](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@15.0/api/UnityEngine.Rendering.DebugManager.html#UnityEngine_Rendering_DebugManager_GetPanel_System_String_System_Boolean_System_Int32_System_Boolean_).
  5. Add the widget to an array.
  6. Add the widget array to the list of children in the panel.

If you add 2 or more widgets to the array, the panel displays the widgets in
the same order as the array.

The following code sample creates and adds a widget that enables or disables
the main directional light:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections.Generic;
    using System.Linq;
    
    [ExecuteInEditMode]
    public class CustomDebugPanel : MonoBehaviour
    {
    
        static bool lightEnabled = true;
    
        void OnEnable()
        {
            // Create a list of widgets
            var widgetList = new List<DebugUI.Widget>();
    
            // Add a checkbox widget to the list of widgets
            widgetList.AddRange(new DebugUI.Widget[]
            {
                new DebugUI.BoolField
                {
                    displayName = "Enable main directional light",
                    tooltip = "Enable or disable the main directional light",
                    getter = () => lightEnabled,
    
                    // When the widget value is changed, change the value of lightEnabled
                    setter = value => lightEnabled = value,
    
                    // Run a custom function to enable or disable the main directional light based on the widget value
                    onValueChanged = DisplaySunChanged
                },
            });
    
            // Create a new panel (tab) in the Rendering Debugger
            var panel = DebugManager.instance.GetPanel("My Custom Panel", createIfNull: true);
    
            // Add the widgets to the panel
            panel.children.Add(widgetList.ToArray());
        }
    
        // Remove the custom panel if the GameObject is disabled
        void OnDisable()
        {
            DebugManager.instance.RemovePanel("My Custom Panel");
        }
    
        // Enable or disable the main directional light based on the widget value
        void DisplaySunChanged(DebugUI.Field<bool> field, bool displaySun)
        {
            Light sun = FindObjectsOfType<Light>().Where(x => x.type == LightType.Directional).FirstOrDefault();
            if (sun)
                sun.enabled = displaySun;
        }
    }
    

Add the script to a **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject). You should notice a new
**My Custom Panel** panel in the **Rendering Debugger** window.

### Add a control to an existing panel

To fetch an existing panel, use `DebugManager.instance.GetPanel` with the
panel name. Set `createIfNull` to `false`, so you don’t accidentally create a
new panel if the name doesn’t match an existing panel.

The following code sample fetches the panel from the code sample above:

    
    
    var panel = DebugManager.instance.GetPanel("My Custom Panel", createIfNull: false);
    

You shouldn’t add widgets to [URP’s built-in Rendering Debugger
panels](rendering-debugger.html).

## Add a container

You can use containers to display groups of widgets together.

  1. Create a container using one of the child classes of [DebugUI.Container](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@15.0/api/UnityEngine.Rendering.DebugUI.Container.html), for example `DebugUI.Foldout`.
  2. Add a widget array using the container’s `Add` method.

The following code sample creates a collapsible container that contains 2
checkboxes:

    
    
    using UnityEngine;
    using UnityEngine.Rendering;
    using System.Collections.Generic;
    
    [ExecuteInEditMode]
    public class CustomDebugPanelWithContainer : MonoBehaviour
    {
        void OnEnable()
        {
            // Create a list of widgets
            var widgetList = new List<DebugUI.Widget>();
    
            // Add 2 checkbox widgets to the list of widgets
            widgetList.AddRange(new DebugUI.Widget[]
            {
                new DebugUI.BoolField
                {
                    displayName = "Visualisation 1",
                },
                new DebugUI.BoolField
                {
                    displayName = "Visualisation 2",
                },
            });
    
            // Create a container
            var container = new DebugUI.Foldout
            {
                displayName = "My Container"
            };
    
            // Add the widgets to the container
            container.children.Add(widgetList.ToArray());
    
            // Create a new panel (tab) in the Rendering Debugger
            var panel = DebugManager.instance.GetPanel("My Custom Panel With Container", createIfNull: true);
    
            // Add the container to the panel
            panel.children.Add(container);
        }
    }
    

[](../../urp/features/rendering-debugger-use.html)

Enable the Rendering Debugger in URP

[](../../urp/features/rendering-debugger-reference.html)

Rendering Debugger window reference for URP

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

