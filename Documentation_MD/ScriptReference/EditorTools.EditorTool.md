[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# EditorTool

class in UnityEditor.EditorTools

/

Inherits from:[ScriptableObject](ScriptableObject.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Use this class to implement editor tools. This is the base class from which
all editor tools are inherited.

Use this class with
[EditorToolAttribute](EditorTools.EditorToolAttribute.html) to register custom
editor tools with the Editor.  
  
There are two basic types of tools, Global and Component. See
[EditorToolAttribute](EditorTools.EditorToolAttribute.html) for information on
how to designate a tool as Global or Component.  
  
Global tools are like the built-in Move, Rotate, Scale tools. They are always
available, and work with whatever is in the current
[Selection](Selection.html).  
  
Component tools, similar to [CustomEditor](CustomEditor.html), are specific to
a [Component](Component.html). These tools are made available when the active
selection contains an editable type.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEditor.ShortcutManagement;
    using UnityEngine;  
      
    // Example [MonoBehaviour](MonoBehaviour.html) that oscillates a transform position between two points.
    public class Platform : [MonoBehaviour](MonoBehaviour.html)
    {
        [[SerializeField](SerializeField.html)]
        [Vector3](Vector3.html) m_Start = new [Vector3](Vector3.html)(-10, 0f, 0f);  
      
        [[SerializeField](SerializeField.html)]
        [Vector3](Vector3.html) m_End = new [Vector3](Vector3.html)(10f, 0f, 0f);  
      
        [[SerializeField](SerializeField.html)]
        float m_Speed = .2f;  
      
        public [Vector3](Vector3.html) start
        {
            get => m_Start;
            set => m_Start = value;
        }  
      
        public [Vector3](Vector3.html) end
        {
            get => m_End;
            set => m_End = value;
        }  
      
        public float speed
        {
            get => m_Speed;
            set => m_Speed = value;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            SnapToPath([Time.time](Time-time.html));
        }  
      
        public void SnapToPath(float time)
        {
            transform.position = [Vector3.Lerp](Vector3.Lerp.html)(m_Start, m_End, ([Mathf.Sin](Mathf.Sin.html)(time * m_Speed) + 1) * .5f);
        }
    }  
      
    // The second argument in the [EditorToolAttribute](EditorTools.EditorToolAttribute.html) flags this as a [Component](Component.html) tool. That means that it will be instantiated
    // and destroyed along with the selection. [EditorTool.targets](EditorTools.EditorTool-targets.html) will contain the selected objects matching the type.
    [[EditorTool](EditorTools.EditorTool.html)("Platform [Tool](Tool.html)", typeof(Platform))]
    class PlatformTool : [EditorTool](EditorTools.EditorTool.html), [IDrawSelectedHandles](EditorTools.IDrawSelectedHandles.html)
    {
        // Enable or disable preview animation
        bool m_AnimatePlatforms;  
      
        // Global tools (tools that do not specify a target type in the attribute) are lazy initialized and persisted by
        // a [ToolManager](EditorTools.ToolManager.html). [Component](Component.html) tools (like this example) are instantiated and destroyed with the current selection.
        void OnEnable()
        {
            // Allocate unmanaged resources or perform one-time set up functions here
        }  
      
        void OnDisable()
        {
            // Free unmanaged resources, state teardown.
        }  
      
        // The second "context" argument accepts an [EditorWindow](EditorWindow.html) type.
        [Shortcut("Activate Platform [Tool](Tool.html)", typeof([SceneView](SceneView.html)), [KeyCode.P](KeyCode.P.html))]
        static void PlatformToolShortcut()
        {
            if ([Selection.GetFiltered](Selection.GetFiltered.html)<Platform>([SelectionMode.TopLevel](SelectionMode.TopLevel.html)).[Length](UIElements.Length.html) > 0)
                [ToolManager.SetActiveTool](EditorTools.ToolManager.SetActiveTool.html)<PlatformTool>();
            else
                [Debug.Log](Debug.Log.html)("No platforms selected!");
        }  
      
        // Called when the active tool is set to this tool instance. Global tools are persisted by the [ToolManager](EditorTools.ToolManager.html),
        // so usually you would use OnEnable and OnDisable to manage native resources, and OnActivated/OnWillBeDeactivated
        // to set up state. See also `EditorTools.{ activeToolChanged, activeToolChanged }` events.
        public override void OnActivated()
        {
            SceneView.lastActiveSceneView.ShowNotification(new [GUIContent](GUIContent.html)("Entering Platform [Tool](Tool.html)"), .1f);
        }  
      
        // Called before the active tool is changed, or destroyed. The exception to this rule is if you have manually
        // destroyed this tool (ex, calling `Destroy(this)` will skip the OnWillBeDeactivated invocation).
        public override void OnWillBeDeactivated()
        {
            SceneView.lastActiveSceneView.ShowNotification(new [GUIContent](GUIContent.html)("Exiting Platform [Tool](Tool.html)"), .1f);
        }  
      
        // Equivalent to [Editor.OnSceneGUI](Editor.OnSceneGUI.html).
        public override void OnToolGUI([EditorWindow](EditorWindow.html) window)
        {
            if (!(window is [SceneView](SceneView.html) sceneView))
                return;  
      
            [Handles.BeginGUI](Handles.BeginGUI.html)();
            using (new [GUILayout.HorizontalScope](GUILayout.HorizontalScope.html)())
            {
                using (new [GUILayout.VerticalScope](GUILayout.VerticalScope.html)([EditorStyles.helpBox](EditorStyles-helpBox.html)))
                {
                    m_AnimatePlatforms = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Animate Platforms", m_AnimatePlatforms);
                    // To animate platforms we need the [Scene](SceneManagement.Scene.html) View to repaint at fixed intervals, so enable `alwaysRefresh`
                    // and scene FX (need both for this to work). In older versions of Unity this is called `materialUpdateEnabled`
                    sceneView.sceneViewState.alwaysRefresh = m_AnimatePlatforms;
                    if (m_AnimatePlatforms && !sceneView.sceneViewState.fxEnabled)
                        sceneView.sceneViewState.fxEnabled = true;  
      
                    if ([GUILayout.Button](GUILayout.Button.html)("Snap to Path"))
                        foreach (var obj in targets)
                            if (obj is Platform platform)
                                platform.SnapToPath((float)[EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html));
                }  
      
                [GUILayout.FlexibleSpace](GUILayout.FlexibleSpace.html)();
            }
            [Handles.EndGUI](Handles.EndGUI.html)();  
      
            foreach (var obj in targets)
            {
                if (!(obj is Platform platform))
                    continue;  
      
                if (m_AnimatePlatforms && Event.current.type == [EventType.Repaint](EventType.Repaint.html))
                    platform.SnapToPath((float)[EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html));  
      
                [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
                var start = [Handles.PositionHandle](Handles.PositionHandle.html)(platform.start, [Quaternion.identity](Quaternion-identity.html));
                var end = [Handles.PositionHandle](Handles.PositionHandle.html)(platform.end, [Quaternion.identity](Quaternion-identity.html));
                if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
                {
                    [Undo.RecordObject](Undo.RecordObject.html)(platform, "Set Platform Destinations");
                    platform.start = start;
                    platform.end = end;
                }
            }
        }  
      
        // [IDrawSelectedHandles](EditorTools.IDrawSelectedHandles.html) interface allows tools to draw gizmos when the target objects are selected, but the tool
        // has not yet been activated. This allows you to keep [MonoBehaviour](MonoBehaviour.html) free of debug and gizmo code.
        public void OnDrawHandles()
        {
            foreach (var obj in targets)
            {
                if (obj is Platform platform)
                    [Handles.DrawLine](Handles.DrawLine.html)(platform.start, platform.end, 6f);
            }
        }
    }
    

### Properties

[gridSnapEnabled](EditorTools.EditorTool-gridSnapEnabled.html)| Use this
property to allow the current EditorTool to enable/disable grid snapping.  
---|---  
[target](EditorTools.EditorTool-target.html)| The object being inspected.  
[targets](EditorTools.EditorTool-targets.html)| An array of the objects being
inspected.  
[toolbarIcon](EditorTools.EditorTool-toolbarIcon.html)| The icon and tooltip
for this custom editor tool. If this function is not implemented, the toolbar
displays the Inspector icon for the target type. If no target type is defined,
the toolbar displays the Tool Mode icon.  
  
### Public Methods

[IsAvailable](EditorTools.EditorTool.IsAvailable.html)| Checks whether the
custom editor tool is available based on the state of the editor.  
---|---  
[OnActivated](EditorTools.EditorTool.OnActivated.html)| Invoked after this
EditorTool becomes the active tool.  
[OnToolGUI](EditorTools.EditorTool.OnToolGUI.html)| Use this method to
implement a custom editor tool.  
[OnWillBeDeactivated](EditorTools.EditorTool.OnWillBeDeactivated.html)|
Invoked before this EditorTool stops being the active tool.  
[PopulateMenu](EditorTools.EditorTool.PopulateMenu.html)| Adds menu items to
Scene view context menu.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

