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

# EditorToolContext

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

Use this class to implement specialized versions of the built-in transform
tools. Built-in transform tools include Move, Rotate, Scale, Rect, and
Transform.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.EditorTools;
    using UnityEngine;
    // [EditorToolContextAttribute](EditorTools.EditorToolContextAttribute.html) is what registers a context with the UI.
    [[EditorToolContext](EditorTools.EditorToolContext.html)("Wobbly [Transform](Transform.html) [Tools](Tools.html)")]
    // The icon path can also be used with packages. Ex "Packages/com.wobblestudio.wobblytools/Icons/Transform.png".
    [Icon("Assets/Examples/Icons/TransformIcon.png")]
    public class WobbleContext : [EditorToolContext](EditorTools.EditorToolContext.html)
    {
        // [Tool](Tool.html) contexts can also implement an OnToolGUI function that is invoked before tools. This is a good place to
        // add any custom selection logic, for example.
        public override void OnToolGUI([EditorWindow](EditorWindow.html) _) { }
        protected override Type GetEditorToolType([Tool](Tool.html) tool)
        {
            switch (tool)
            {
                // Return the type of tool to be used for [Tool.Move](Tool.Move.html). The [Tool](Tool.html) Manager will handle instantiating and
                // activating the tool.
                case [Tool.Move](Tool.Move.html):
                    return typeof(WobblyMoveTool);
                // For any tools that are not implemented, return null to disable the tool in the menu.
                default:
                    return null;
            }
        }
    }
    // Note that tools used by an [EditorToolContext](EditorTools.EditorToolContext.html) do not need to use [EditorToolAttribute](EditorTools.EditorToolAttribute.html).
    class WobblyMoveTool : [EditorTool](EditorTools.EditorTool.html)
    {
        struct Selected
        {
            public [Transform](Transform.html) transform;
            public [Vector3](Vector3.html) localScale;
        }
        [Vector3](Vector3.html) m_Origin;
        List<Selected> m_Selected = new List<Selected>();
        void StartMove([Vector3](Vector3.html) origin)
        {
            m_Origin = origin;
            m_Selected.Clear();
            foreach(var trs in [Selection.transforms](Selection-transforms.html))
                m_Selected.Add(new Selected() { transform = trs, localScale = trs.localScale });
            [Undo.RecordObjects](Undo.RecordObjects.html)([Selection.transforms](Selection-transforms.html), "Wobble Move [Tool](Tool.html)");
        }
        // This is silly example that oscillates the scale of the selected objects as they are moved.
        public override void OnToolGUI([EditorWindow](EditorWindow.html) _)
        {
            var evt = Event.current.type;
            var hot = [GUIUtility.hotControl](GUIUtility-hotControl.html);
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();
            var p = [Handles.PositionHandle](Handles.PositionHandle.html)([Tools.handlePosition](Tools-handlePosition.html), [Tools.handleRotation](Tools-handleRotation.html));
            if (evt == [EventType.MouseDown](EventType.MouseDown.html) && hot != [GUIUtility.hotControl](GUIUtility-hotControl.html))
                StartMove(p);
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                foreach (var selected in m_Selected)
                {
                    selected.transform.position += (p - [Tools.handlePosition](Tools-handlePosition.html));
                    var scale = [Vector3.one](Vector3-one.html) * ([Mathf.Sin](Mathf.Sin.html)([Mathf.Abs](Mathf.Abs.html)([Vector3.Distance](Vector3.Distance.html)(m_Origin, p))) * .5f);
                    selected.transform.localScale = selected.localScale + scale;
                }
            }
        }
    }
    

### Properties

[target](EditorTools.EditorToolContext-target.html)| The object being
inspected.  
---|---  
[targets](EditorTools.EditorToolContext-targets.html)| An array of the objects
being inspected.  
  
### Public Methods

[GetAdditionalToolTypes](EditorTools.EditorToolContext.GetAdditionalToolTypes.html)|
Get an additional collection of tools to display in the same category as the
built-in transform tools.  
---|---  
[OnActivated](EditorTools.EditorToolContext.OnActivated.html)| Invoked after
this EditorToolContext becomes the active tool context.  
[OnToolGUI](EditorTools.EditorToolContext.OnToolGUI.html)| Implements any
common functionality for the set of manipulation tools available for this
context.  
[OnWillBeDeactivated](EditorTools.EditorToolContext.OnWillBeDeactivated.html)|
Invoked before this EditorToolContext stops being the active tool context.  
[PopulateMenu](EditorTools.EditorToolContext.PopulateMenu.html)| Adds menu
items to the Scene view context menu.  
[ResolveTool](EditorTools.EditorToolContext.ResolveTool.html)| Returns the
matching EditorTool type for the specified Tool given the context.  
  
### Protected Methods

[GetEditorToolType](EditorTools.EditorToolContext.GetEditorToolType.html)|
Defines the EditorTool type for a given Tool.  
---|---  
  
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

