[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SupportingPresets.html)
  * [中文](/cn/current/Manual/SupportingPresets.html)
  * [日本語](/ja/current/Manual/SupportingPresets.html)
  * [한국어](/kr/current/Manual/SupportingPresets.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SupportingPresets.html)
  * [中文](/cn/current/Manual/SupportingPresets.html)
  * [日本語](/ja/current/Manual/SupportingPresets.html)
  * [한국어](/kr/current/Manual/SupportingPresets.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Presets](Presets.html)
  * Supporting presets

[](Presets.html)

Presets

[](DefaultPresetsByFolder.html)

Applying default presets to Assets by folder

## Supporting presets

In your Editor **scripts** A piece of code that allows you to create your own
Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), use the
[ObjectFactory](../ScriptReference/ObjectFactory.html) class to create new
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject), components and Assets. When
creating these items, the `ObjectFactory` class automatically uses default
Presets. Your script does not have to search for and apply default
[Presets](Presets.html), because `ObjectFactory` handles this for you.

## Support for new types

To support and enable Presets by default, your class must inherit from one of
the following:

  * [UnityEngine.Monobehaviour](../ScriptReference/MonoBehaviour.html)
  * [UnityEngine.ScriptableObject](../ScriptReference/ScriptableObject.html)
  * [UnityEngine.ScriptedImporter](../ScriptReference/AssetImporters.ScriptedImporter.html)

The Preset **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) creates a temporary instance of
your class, so that users can modify its values, so make sure your class does
not affect or rely on other objects such as static values, Project Assets or
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) instances.

**Tip** : Using a [CustomEditor](../ScriptReference/CustomEditor.html)
attribute is optional.

## Use case example: Preset settings in a custom Editor window

When setting up a custom [EditorWindow](../ScriptReference/EditorWindow.html)
class with settings that could use Presets:

  * Use a [ScriptableObject](../ScriptReference/ScriptableObject.html) to store a copy of your settings. It can have a [CustomEditor](../ScriptReference/CustomEditor.html) attribute too. The Preset system handles this object.

  * Always use this temporary `ScriptableObject` Inspector to show the Preset settings in your **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI). This allows your users to have the same
UI in your `EditorWindow` and when editing saved Presets.

  * Expose a Preset button and use your own [PresetSelectorReceiver](../ScriptReference/Presets.PresetSelectorReceiver.html) implementation to keep your `EditorWindow` settings up-to-date when a Preset is selected in the **Select Preset** window.

The following script examples demonstrate how to add Preset settings to a
simple `EditorWindow`.

This script example demonstrates a ScriptableObject that keeps and shows
settings in a custom window (saved to a file called
_Editor/MyWindowSettings.cs_):

    
    
    using UnityEngine;
    
    // Temporary ScriptableObject used by the Preset system
    
    public class MyWindowSettings : ScriptableObject
    {
        [SerializeField]
        string m_SomeSettings;
        
        public void Init(MyEditorWindow window)
        {
            m_SomeSettings = window.someSettings;
        }
        
        public void ApplySettings(MyEditorWindow window)
        {
            window.someSettings = m_SomeSettings;
            window.Repaint();
        }
    }
    

Script example of a `PresetSelectorReceiver` that updates the
`ScriptableObject` used in the custom window (saved to a file called
_Editor/MySettingsReceiver.cs)_ :

    
    
    using UnityEditor.Presets;
    
    // PresetSelector receiver to update the EditorWindow with the selected values.
    
    public class MySettingsReceiver : PresetSelectorReceiver
    {
        Preset initialValues;
        MyWindowSettings currentSettings;
        MyEditorWindow currentWindow;
        
        public void Init(MyWindowSettings settings, MyEditorWindow window)
        {
            currentWindow = window;
            currentSettings = settings;
            initialValues = new Preset(currentSettings);
        }
        
        public override void OnSelectionChanged(Preset selection)
        {
            if (selection != null)
            {
                // Apply the selection to the temporary settings
                selection.ApplyTo(currentSettings);
            }
            else
            {
                // None have been selected. Apply the Initial values back to the temporary selection.
                initialValues.ApplyTo(currentSettings);
            }
            
            // Apply the new temporary settings to our manager instance
            currentSettings.ApplySettings(currentWindow);
        }
        
        public override void OnSelectionClosed(Preset selection)
        {
            // Call selection change one last time to make sure you have the last selection values.
            OnSelectionChanged(selection);
            // Destroy the receiver here, so you don't need to keep a reference to it.
            DestroyImmediate(this);
        }
    }
    

Script example of an [EditorWindow](../ScriptReference/EditorWindow.html) that
shows custom settings using a temporary ScriptableObject Inspector and its
Preset button (saved to a file called _Editor/MyEditorWindow.cs)_ :

    
    
    using UnityEngine;
    using UnityEditor;
    using UnityEditor.Presets;
    
    public class MyEditorWindow : EditorWindow
    
    {
        // get the Preset icon and a style to display it
        private static class Styles
        {
            public static GUIContent presetIcon = EditorGUIUtility.IconContent("Preset.Context");
            public static GUIStyle iconButton = new GUIStyle("IconButton");
    
        }
    
        Editor m_SettingsEditor;
        MyWindowSettings m_SerializedSettings;
        
        public string someSettings
        {
            get { return EditorPrefs.GetString("MyEditorWindow_SomeSettings"); }
            set { EditorPrefs.SetString("MyEditorWindow_SomeSettings", value); }
        }
       
        // Method to open the window
        [MenuItem("Window/MyEditorWindow")]
        static void OpenWindow()
        {
            GetWindow<MyEditorWindow>();
        }
    
        void OnEnable()
        {
            // Create your settings now and its associated Inspector
            // that allows to create only one custom Inspector for the settings in the window and the Preset.
            m_SerializedSettings = ScriptableObject.CreateInstance<MyWindowSettings>();
            m_SerializedSettings.Init(this);
            m_SerializedSettings.hideFlags = HideFlags.DontSave;
            m_SettingsEditor = Editor.CreateEditor(m_SerializedSettings);
            m_SettingsEditor.hideFlags = HideFlags.DontSave;
        }
    
        void OnDisable()
        {
            Object.DestroyImmediate(m_SerializedSettings);
            Object.DestroyImmediate(m_SettingsEditor);
        }
    
        void OnGUI()
        {
            EditorGUILayout.BeginHorizontal();
            EditorGUILayout.LabelField("My custom settings", EditorStyles.boldLabel);
            GUILayout.FlexibleSpace();
            // create the Preset button at the end of the "MyManager Settings" line.
            var buttonPosition = EditorGUILayout.GetControlRect(false, EditorGUIUtility.singleLineHeight, Styles.iconButton);
    
            if (EditorGUI.DropdownButton(buttonPosition, Styles.presetIcon, FocusType.Passive, Styles.iconButton))
            {
                // Create a receiver instance. This destroys itself when the window appears, so you don't need to keep a reference to it.
                var presetReceiver = ScriptableObject.CreateInstance<MySettingsReceiver>();
                presetReceiver.Init(m_SerializedSettings, this);
                // Show the PresetSelector modal window. The presetReceiver updates your data.
                PresetSelector.ShowSelector(m_SerializedSettings, null, true, presetReceiver);
            }
            EditorGUILayout.EndHorizontal();
            
            // Draw the settings default Inspector and catch any change made to it.
            EditorGUI.BeginChangeCheck();
            m_SettingsEditor.OnInspectorGUI();
    
            if (EditorGUI.EndChangeCheck())
            {
                // Apply changes made in the settings editor to our instance.
                m_SerializedSettings.ApplySettings(this);
            }
        }
    }
    

* * *

2017–03–27 Page published  New feature in
[2018.1](https://docs.unity3d.com/2018.1/Documentation/Manual/30_search.html?q=newin20181)
NewIn20181

[](Presets.html)

Presets

[](DefaultPresetsByFolder.html)

Applying default presets to Assets by folder

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

