[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/overlays-custom.html)
  * [中文](/cn/current/Manual/overlays-custom.html)
  * [日本語](/ja/current/Manual/overlays-custom.html)
  * [한국어](/kr/current/Manual/overlays-custom.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/overlays-custom.html)
  * [中文](/cn/current/Manual/overlays-custom.html)
  * [日本語](/ja/current/Manual/overlays-custom.html)
  * [한국어](/kr/current/Manual/overlays-custom.html)

  * [The Unity Editor](unity-editor.html)
  * [Unity's interface](UsingTheEditor.html)
  * [The Scene view](UsingTheSceneView.html)
  * [Overlays](overlays.html)
  * Create your own overlay

[](cameras-overlay.html)

Cameras overlay

[](GridSnapping.html)

Scene view grid snapping

# Create your own overlay

You can create custom panel overlays and **toolbar** A row of buttons and
basic controls at the top of the Unity Editor that allows you to interact with
the Editor in various ways (e.g. scaling, translation). [More
info](Toolbar.html)  
See in [Glossary](Glossary.html#Toolbar) overlays for the ****Scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view** window.

  * Panel Overlays
  * Toolbar Overlays

**Tip** : For information about creating UIElements, refer to the [UI Elements
Developer Guide](https://docs.unity3d.com/Manual/UIElements.html).

## Understand EditorToolbarElement

A toolbar element can contain text, an icon, or a combination of both.

Use `EditorToolbarElement(Identifier, EditorWindowType)` to register toolbar
elements to use in `ToolbarOverlay` implementations.

You can inherit from any `VisualElement` type and create styling yourself, but
toolbar elements require specific styling. It is preferable to inherit from
one of these predefined `EditorToolbar` types:

  * `EditorToolbarButton`: Based on `UnityEditor.UIElements.ToolbarButton`
  * `EditorToolbarToggle`: Based on `UnityEditor.UIElements.ToolbarToggle`
  * `EditorToolbarDropdown`: Based on `EditorToolbarButton`
  * `EditorToolbarDropdownToggle`: Based on `UnityEngine.UIElements.BaseField`

**Tip:** If a toolbar is docked horizontally or vertically, its text might not
be visible or clipped. You can specify an icon for each toolbar to avoid text
clipping.

## Create a panel overlay

All overlays must inherit from the
[Overlay](../ScriptReference/Overlays.Overlay.html) base class and implement
the
[CreatePanelContent](../ScriptReference/Overlays.Overlay.CreatePanelContent.html)
method. This creates a basic panel that you can use and that you can add
toolbar elements to.

To create a panel overlay:

  1. Create a new [C# script](creating-scripts.html) in the [Editor folder](SpecialFolders.html) and name it.

  2. Open the script you created.

  3. Remove the default content from the script.

  4. Implement the `Overlay` class from the `UnityEditor.Overlays` namespace.

  5. Override the [CreatePanelContent](../ScriptReference/Overlays.Overlay.CreatePanelContent.html) function and add your content to the **visual element** A node of a visual tree that instantiates or derives from the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You can style the look, define the behaviour, and display it on screen as part of the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement).

  6. Add the [OverlayAttribute](../ScriptReference/Overlays.OverlayAttribute.html) attribute to the class.

  7. In the `OverlayAttribute`, specify which type of window you want this overlay to be in:

     * If you want the overlay to be available in all Editor windows, specify `EditorWindow` as the type.
     * If you want the overlay to only be available in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView), specify `SceneView` as the type.

  8. In the `OverlayAttribute`, add a name, ID, and display name to the overlay. 

  9. To add an icon that displays when your overlay is collapsed, add the `Icon` attribute to the `Overlay` class and specify an icon. If the overlay has no icon, then by default the system uses the first two letters of the overlay name or the first two initial letters of the first two words. 

### Example

    
    
    using UnityEditor;
    using UnityEditor.Overlays;
    using UnityEngine.UIElements;
    [Overlay(typeof(SceneView), "Panel Overlay Example", true)]
    public class MyToolButtonOverlay : Overlay
    {
        public override VisualElement CreatePanelContent()
        {
            var root = new VisualElement() { name = "My Toolbar Root" };
            root.Add(new Label() { text = "Hello" });
            return root;
    
        }
    }
    

## Create a toolbar overlay

Toolbar overlays are containers that hold toolbar items and are composed of
collections of `EditorToolbarElement`.

Toolbar overlays have built-in horizontal, vertical, and panel layouts.
`ToolbarOverlay` implements a parameterless constructor that passes the
`EditorToolbarElementAttribute` ID. Unlike panel overlays, the contents are
defined as standalone pieces that are collected to form a strip of elements.

When you create toolbar overlays:

  * Use `EditorToolbarElement(Identifier, EditorWindowType)` to register toolbar elements to use in the `ToolbarOverlay` implementation.
  * Tag all overlays with [OverlayAttribute](../ScriptReference/Overlays.OverlayAttribute.html).
  * Make sure that toolbar overlays inherit `ToolbarOverlay` and implement a parameterless constructor.
  * Make sure that the contents of a toolbar are populated with string IDs, which are passed to the base constructor.
  * Make sure that IDs are defined by `EditorToolbarElementAttribute`.
  * Use the `Icon` attribute to add icon an icon to your overlay. The icon is visible when an overlay is collapsed. If the overlay does not have an icon, the first two letters of the overlay name (or the first two initial letters of the first two words) are shown when the overlay is collapsed.

When you implement elements specific to `ToolbarOverlay` in an overlay:

  * Use the `IAccessContainerWindow` interface for toolbars only. The element is not aware of its context. In the `DropdownToggleExample`, if you toggle the element it won’t do anything.
  * Use `UIElement` styling for visuals. The toolbar element won’t have its styling in an overlay.

To create a toolbar overlay:

  1. Create a new [C# script](creating-scripts.html) in the [Editor folder](SpecialFolders.html) and name it.
  2. Open the script you created.
  3. Remove the default content from the script.
  4. Add toolbar elements to the script.
  5. Add toolbar elements to the overlay constructor.
  6. Add the panel overlay and implement the toolbar elements.

### Example

This example is of an overlay named **Element Toolbars Example** that
demonstrates these toolbar elements:

  * `EditorToolbarButton`
  * `EditorToolbarToggle`
  * `EditorToolbarDropdown`
  * `EditorToolbarDropdownToggle`

Each toolbar element is created as a standalone class and then added to the
overlay panel.

This overlay:

  * Can be arranged as a panel, horizontally, and vertically.
  * Has buttons that include text and tooltips.
  * Has toolbar icons defined by the `Icon` attribute. This icon displays when the overlay is collapsed.

    
    
        using System.Collections;
        using System.Collections.Generic;
        using System.Text;
        using UnityEngine;
        using UnityEditor.EditorTools;
        using UnityEditor.Toolbars;
        using UnityEditor.Overlays;
        using UnityEngine.UIElements;
        using UnityEditor;
    
        // Use [EditorToolbarElement(Identifier, EditorWindowType)] to register toolbar elements for use in ToolbarOverlay implementation.
    
        [EditorToolbarElement(id, typeof(SceneView))]
        class DropdownExample : EditorToolbarDropdown
        {
            public const string id = "ExampleToolbar/Dropdown";
    
            static string dropChoice = null;
    
            public DropdownExample()
            {
                text = "Axis";
                clicked += ShowDropdown;
            }
    
            void ShowDropdown()
            {
                var menu = new GenericMenu();
                menu.AddItem(new GUIContent("X"), dropChoice == "X", () => { text = "X"; dropChoice = "X"; });
                menu.AddItem(new GUIContent("Y"), dropChoice == "Y", () => { text = "Y"; dropChoice = "Y"; });
                menu.AddItem(new GUIContent("Z"), dropChoice == "Z", () => { text = "Z"; dropChoice = "Z"; });
                menu.ShowAsContext();
            }
        }
        [EditorToolbarElement(id, typeof(SceneView))]
        class ToggleExample : EditorToolbarToggle
        {
            public const string id = "ExampleToolbar/Toggle";
            public ToggleExample()
            {
                text = "Toggle OFF";
                this.RegisterValueChangedCallback(Test);
            }
    
            void Test(ChangeEvent<bool> evt)
            {
                if (evt.newValue)
                {
                    Debug.Log("ON");
                    text = "Toggle ON";
                }
                else
                {
                    Debug.Log("OFF");
                    text = "Toggle OFF";
                }
            }
        }
    
        [EditorToolbarElement(id, typeof(SceneView))]
        class DropdownToggleExample : EditorToolbarDropdownToggle, IAccessContainerWindow
        {
            public const string id = "ExampleToolbar/DropdownToggle";
    
            // This property is specified by IAccessContainerWindow and is used to access the Overlay's EditorWindow.
    
            public EditorWindow containerWindow { get; set; }
            static int colorIndex = 0;
            static readonly Color[] colors = new Color[] { Color.red, Color.green, Color.cyan };
            public DropdownToggleExample()
            {
                text = "Color Bar";
                tooltip = "Display a color rectangle in the top left of the Scene view. Toggle on or off, and open the dropdown" +
                          "to change the color.";
    
            // When the dropdown is opened, ShowColorMenu is invoked and we can create a popup menu.
    
                dropdownClicked += ShowColorMenu;
    
            // Subscribe to the Scene view OnGUI callback so that we can draw our color swatch.
    
                SceneView.duringSceneGui += DrawColorSwatch;
            }
    
            void DrawColorSwatch(SceneView view)
            {
    
             // Test that this callback is for the Scene View that we're interested in, and also check if the toggle is on
            // or off (value).
    
                if (view != containerWindow || !value)
                {
                    return;
                }
    
                Handles.BeginGUI();
                GUI.color = colors[colorIndex];
                GUI.DrawTexture(new Rect(8, 8, 120, 24), Texture2D.whiteTexture);
                GUI.color = Color.white;
                Handles.EndGUI();
            }
    
            // When the dropdown button is clicked, this method will create a popup menu at the mouse cursor position.
    
            void ShowColorMenu()
            {
                var menu = new GenericMenu();
                menu.AddItem(new GUIContent("Red"), colorIndex == 0, () => colorIndex = 0);
                menu.AddItem(new GUIContent("Green"), colorIndex == 1, () => colorIndex = 1);
                menu.AddItem(new GUIContent("Blue"), colorIndex == 2, () => colorIndex = 2);
                menu.ShowAsContext();
            }
        }
    
        [EditorToolbarElement(id, typeof(SceneView))]
        class CreateCube : EditorToolbarButton//, IAccessContainerWindow
        {
            // This ID is used to populate toolbar elements.
    
            public const string id = "ExampleToolbar/Button";
    
            // IAccessContainerWindow provides a way for toolbar elements to access the `EditorWindow` in which they exist.
            // Here we use `containerWindow` to focus the camera on our newly instantiated objects after creation.
            //public EditorWindow containerWindow { get; set; }
    
            // Because this is a VisualElement, it is appropriate to place initialization logic in the constructor.
            // In this method you can also register to any additional events as required. In this example there is a tooltip, an icon, and an action.
    
            public CreateCube()
            {
    
        // A toolbar element can be either text, icon, or a combination of the two. Keep in mind that if a toolbar is
            // docked horizontally the text will be clipped, so usually it's a good idea to specify an icon.
    
                text = "Create Cube";
                icon = AssetDatabase.LoadAssetAtPath<Texture2D>("Assets/CreateCubeIcon.png");
                tooltip = "Instantiate a cube in the scene.";
                clicked += OnClick;
            }
    
            // This method will be invoked when the `Create Cube` button is clicked.
    
            void OnClick()
            {
                var newObj = GameObject.CreatePrimitive(PrimitiveType.Cube).transform;
    
            // When writing editor tools don't forget to be a good citizen and implement Undo!
    
                Undo.RegisterCreatedObjectUndo(newObj.gameObject, "Create Cube");
    
            //if (containerWindow is SceneView view)
            //    view.FrameSelected();
    
            }
    
        }
    
        // All Overlays must be tagged with the OverlayAttribute
    
        [Overlay(typeof(SceneView), "ElementToolbars Example")]
    
            // IconAttribute provides a way to define an icon for when an Overlay is in collapsed form. If not provided, the name initials are used.
    
        [Icon("Assets/unity.png")]
    
        // Toolbar Overlays must inherit `ToolbarOverlay` and implement a parameter-less constructor. The contents of a toolbar are populated with string IDs, which are passed to the base constructor. IDs are defined by EditorToolbarElementAttribute.
    
        public class EditorToolbarExample : ToolbarOverlay
        {
    
         // ToolbarOverlay implements a parameterless constructor, passing the EditorToolbarElementAttribute ID.
        // This is the only code required to implement a toolbar Overlay. Unlike panel Overlays, the contents are defined
        // as standalone pieces that will be collected to form a strip of elements.
    
            EditorToolbarExample() : base(
                CreateCube.id,
                ToggleExample.id,
                DropdownExample.id,
                DropdownToggleExample.id
                )
            { }
        }
    
    
    

## Toolbar elements implementations

The controls for toolbar elements are the same as their equivalent in
UIToolkit, but they inherit some toolbar functionalities and specific styling.

This section has examples of the following toolbar elements:

  * EditorToolbarButton
  * EditorToolbarToggle
  * EditorToolbarDropdown
  * EditorToolbarDropdownToggle

### EditorToolbarButton

`EditorToolbarButton` is a standalone class that contains the logic of the
element. This example creates a button that generates a cube when you click
it:

    
    
    [EditorToolbarElement(id, typeof(SceneView))]
    class CreateCube : EditorToolbarButton
    {
    // This ID is used to populate toolbar elements.
    
    public const string id = "ExampleToolbar/Button";
    
    // Because this is a VisualElement, it is appropriate to place initialization logic in the constructor.
    
    // In this method you can also register to any additional events as required. In this example there is a tooltip, an icon, and an action.
    
        public CreateCube()
           {
    
    // A toolbar element can be either text, icon, or a combination of the two. Keep in mind that if a toolbar is docked horizontally the text will be clipped, so it's a good idea to specify an icon.
    
                text = "Create Cube";
                icon = AssetDatabase.LoadAssetAtPath<Texture2D>("Assets/CreateCubeIcon.png");
                tooltip = "Instantiate a cube in the scene.";
                clicked += OnClick;
    }
    
    void OnClick()
    {
        var newObj = GameObject.CreatePrimitive(PrimitiveType.Cube).transform;
    
        // When writing editor tools, don't forget to be a good citizen and implement Undo.
    
        Undo.RegisterCreatedObjectUndo(newObj.gameObject, "Create Cube");
    
    // Note: Using ObjectFactory class instead of GameObject(like in this example) will register the undo entry automatically removing the need to register manually.
    
    }
    }
    

Add the element’s ID to the Overlay constructor:

    
    
    [Overlay(typeof(SceneView), "ElementToolbar Example")]
    [Icon("Assets/unity.png")]
    public class EditorToolbarExample : ToolbarOverlay
    {
        EditorToolbarExample() : base(CreateCube.id) { }
    
    }
    

### EditorToolbarToggle

Create a standalone class that contains all the logic of the element. This
example creates a toggle that prints its state in the console and updates its
text in the element:

    
    
    [EditorToolbarElement(id, typeof(SceneView))]
    class ToggleExample : EditorToolbarToggle
    {
        public const string id = "ExampleToolbar/Toggle";
        public ToggleExample()
        {
            text = "Toggle OFF";
    
        // Register the class to a callback for when the toggle’s state changes
    
            this.RegisterValueChangedCallback(OnStateChange);
        }
    
        void OnStateChange(ChangeEvent<bool> evt)
        {
            if (evt.newValue)
            {
    
        // Put logic for when the state is ON here
    
                    Debug.Log("Toggle State -> ON");
            text = "Toggle ON";
            }
            else
            {
    
        // Put logic for when the state is OFF here
    
                    Debug.Log("Toggle State -> OFF");
            text = "Toggle OFF";
            }
        }
    }
    

Add the element’s ID to the Overlay constructor:

    
    
    [Overlay(typeof(SceneView), "ElementToolbar Example")]
    [Icon("Assets/unity.png")]
    public class EditorToolbarExample : ToolbarOverlay
    {
        EditorToolbarExample() : base(
    ToggleExample.id
    ) { }
    
    }
    
    

### EditorToolbarDropdown

Create a standalone class that contains all the logic of the element. Here is
a simple example of a dropdown that adjusts its text with the drop-down
selection.

    
    
    [EditorToolbarElement(id, typeof(SceneView))]
    class DropdownExample : EditorToolbarDropdown
    {
        public const string id = "ExampleToolbar/Dropdown";
    
        static string dropChoice = null;
    
        public DropdownExample()
        {
            text = "Axis";
            clicked += ShowDropdown;
        }
    
        void ShowDropdown()
        {
    
    // A simple GenericMenu to populate the dropdown content
    
            var menu = new GenericMenu();
            menu.AddItem(new GUIContent("X"), dropChoice == "X", () => { text = "X"; dropChoice = "X"; });
            menu.AddItem(new GUIContent("Y"), dropChoice == "Y", () => { text = "Y"; dropChoice = "Y"; });
            menu.AddItem(new GUIContent("Z"), dropChoice == "Z", () => { text = "Z"; dropChoice = "Z"; });
            menu.ShowAsContext();
        }
    }
    

Add the element’s ID to the Overlay constructor:

    
    
    [Overlay(typeof(SceneView), "ElementToolbar Example")]
    [Icon("Assets/unity.png")]
    public class EditorToolbarExample : ToolbarOverlay
    {
        EditorToolbarExample() : base(
    DropdownExample.id
    ) { }
    
    }
    

### EditorToolbarDropdownToggle

Create a standalone class that contains all the logic of the element. A
dropdown toggle is a dropdown that can toggled like the **Gizmo** A graphic
overlay associated with a GameObject in a Scene, and displayed in the Scene
View. Built-in scene tools such as the move tool are Gizmos, and you can
create custom Gizmos using textures or scripting. Some Gizmos are only drawn
when the GameObject is selected, while other Gizmos are drawn by the Editor
regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo) menu in the Scene view. This example
creates a rectangle in the corner of the Scene view whos color you can choose
from a dropdown in the overlay.

    
    
    [EditorToolbarElement(id, typeof(SceneView))]
    class DropdownToggleExample : EditorToolbarDropdownToggle, IAccessContainerWindow
    {
        public const string id = "ExampleToolbar/DropdownToggle";
    
    
        // This property is specified by IAccessContainerWindow and is used to access the Overlay's EditorWindow.
    
        public EditorWindow containerWindow { get; set; }
        static int colorIndex = 0;
        static readonly Color[] colors = new Color[] { Color.red, Color.green, Color.cyan };
        public DropdownToggleExample()
        {
            text = "Color Bar";
            tooltip = "Display a color rectangle in the top left of the Scene view. Toggle on or off, and open the dropdown" +
                    "to change the color.";
    
    
       // When the dropdown is opened, ShowColorMenu is invoked and you can create a pop-up menu.
    
            dropdownClicked += ShowColorMenu;
    
    
        // Subscribe to the Scene view OnGUI callback to draw a color swatch.
    
            SceneView.duringSceneGui += DrawColorSwatch;
        }
    
    
        void DrawColorSwatch(SceneView view)
        {
    
            // Test that this callback is for the correct Scene view, and check if the toggle is on
         // or off (value).
    
            if (view != containerWindow || !value)
            {
                return;
            }
    
    
            Handles.BeginGUI();
                GUI.color = colors[colorIndex];
            GUI.DrawTexture(new Rect(8, 8, 120, 24), Texture2D.whiteTexture);
            GUI.color = Color.white;
            Handles.EndGUI();
        }
    
    
        // When the drop-down button is clicked, this method creates a pop-up menu at the mouse cursor position.
    
        void ShowColorMenu()
        {
            var menu = new GenericMenu();
            menu.AddItem(new GUIContent("Red"), colorIndex == 0, () => colorIndex = 0);
            menu.AddItem(new GUIContent("Green"), colorIndex == 1, () => colorIndex = 1);
            menu.AddItem(new GUIContent("Blue"), colorIndex == 2, () => colorIndex = 2);
            menu.ShowAsContext();
        }
    }
    

Add the element’s ID to the Overlay constructor:

    
    
    [Overlay(typeof(SceneView), "ElementToolbar Example")]
    [Icon("Assets/unity.png")]
    public class EditorToolbarExample : ToolbarOverlay
    {
        EditorToolbarExample() : base(
    DropdownToggleExample.id
    ) { }
    
    
    }
    

[](cameras-overlay.html)

Cameras overlay

[](GridSnapping.html)

Scene view grid snapping

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

