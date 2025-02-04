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

# AssetImporterEditor

class in UnityEditor.AssetImporters

/

Inherits from:[Editor](Editor.html)

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

Default editor for all asset importer settings.

Use the default editor to edit the import settings for assets. You can define
a custom import settings editor for a specific asset type. To do this, create
a new class that inherits from AssetImporterEditor and uses a
CustomEditorAttribute that refers to a
[ScriptedImporter](AssetImporters.ScriptedImporter.html).  
  
The following example shows how to make a custom ScriptedImporterEditor for a
ScriptedImporter with a custom layout.

    
    
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(TransformImporter))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class TransformImporterEditor : [ScriptedImporterEditor](AssetImporters.ScriptedImporterEditor.html)
    {
        // Stored [SerializedProperty](SerializedProperty.html) to draw in OnInspectorGUI.
        [SerializedProperty](SerializedProperty.html) m_GenerateChild;  
      
        public override void OnEnable()
        {
            base.OnEnable();
            // Once in OnEnable, retrieve the serializedObject property and store it.
            m_GenerateChild = serializedObject.FindProperty("generateChild");
        }  
      
        public override void OnInspectorGUI()
        {
            // [Update](PlayerLoop.Update.html) the serializedObject in case it has been changed outside the Inspector.
            serializedObject.Update();  
      
            // Draw the boolean property.
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_GenerateChild);  
      
            // Apply the changes so [Undo](Undo.html)/Redo is working
            serializedObject.ApplyModifiedProperties();  
      
            // Call ApplyRevertGUI to show Apply and Revert buttons.
            ApplyRevertGUI();
        }
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(0, ".transform")]
    public class TransformImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public bool generateChild;  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            [GameObject](GameObject.html) root = [ObjectFactory.CreateGameObject](ObjectFactory.CreateGameObject.html)(Path.GetFileNameWithoutExtension(ctx.assetPath));
            if (generateChild)
            {
                [GameObject](GameObject.html) child = [ObjectFactory.CreateGameObject](ObjectFactory.CreateGameObject.html)("child");
                child.transform.SetParent(root.transform);
            }
            ctx.AddObjectToAsset("main", root);
            ctx.SetMainObject(root);
        }
    }
    

The following example demonstrates a specific case where the user cannot
change settings and the Apply/Revert buttons are hidden with
[needsApplyRevert](AssetImporters.AssetImporterEditor-needsApplyRevert.html).

    
    
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine;  
      
    [[CustomEditor](CustomEditor.html)(typeof(EmptinessImporter))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class EmptinessImporterEditor : [ScriptedImporterEditor](AssetImporters.ScriptedImporterEditor.html)
    {
        //Let the parent class know that the Apply/Revert mechanism is skipped.
        protected override bool needsApplyRevert => false;  
      
        public override void OnInspectorGUI()
        {
            // Draw some information
            [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)("Because this Importer doesn't have any settings, the Apply/Revert buttons are hidden.", [MessageType.None](MessageType.None.html));
        }
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(0, ".emptiness")]
    public class EmptinessImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            [GameObject](GameObject.html) root = [ObjectFactory.CreateGameObject](ObjectFactory.CreateGameObject.html)(Path.GetFileNameWithoutExtension(ctx.assetPath));
            ctx.AddObjectToAsset("main", root);
            ctx.SetMainObject(root);
        }
    }
    

The following example shows how to use
[extraDataType](AssetImporters.AssetImporterEditor-extraDataType.html) to read
or save settings that are not part of the ScriptedImporter serialization, in
the custom AssetImporterEditor.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.IO;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;
    using UnityEngine;
    using Object = UnityEngine.Object;  
      
    [[CustomEditor](CustomEditor.html)(typeof(BooleanImporter))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class BooleanImporterEditor : [ScriptedImporterEditor](AssetImporters.ScriptedImporterEditor.html)
    {
        // Property to show in the custom OnInspectorGUI.
        [SerializedProperty](SerializedProperty.html) m_BooleanProperty;  
      
        // override extraDataType to return the type that will be used in the [Editor](Editor.html).
        protected override Type extraDataType => typeof(BooleanClass);  
      
        // override InitializeExtraDataInstance to set up the data.
        protected override void InitializeExtraDataInstance(Object extraTarget, int targetIndex)
        {
            var boolean = (BooleanClass)extraTarget;
            // Read the boolean value from the text file and fill the extraTarget object with the data.
            string fileContent = File.ReadAllText((([AssetImporter](AssetImporter.html))targets[targetIndex]).assetPath);
            if (!bool.TryParse(fileContent, out boolean.boolean))
            {
                boolean.boolean = false;
            }
        }  
      
        protected override void Apply()
        {
            base.Apply();
            // After the Importer is applied, rewrite the file with the custom value.
            for (int i = 0; i < targets.Length; i++)
            {
                string path = (([AssetImporter](AssetImporter.html))targets[i]).assetPath;
                File.WriteAllText(path, ((BooleanClass)extraDataTargets[i]).boolean.ToString());
            }
        }  
      
        public override void OnEnable()
        {
            base.OnEnable();
            // In OnEnable, retrieve the importerUserSerializedObject property and store it.
            m_BooleanProperty = extraDataSerializedObject.FindProperty("boolean");
        }  
      
        public override void OnInspectorGUI()
        {
            // Note: you don't need to call serializedObject.Update or serializedObject.ApplyModifiedProperties
            // because you are not changing the target (serializedObject) itself.  
      
            // [Update](PlayerLoop.Update.html) the importerUserSerializedObject in case it has been changed outside the Inspector.
            extraDataSerializedObject.Update();  
      
            // Draw the boolean property.
            [EditorGUILayout.PropertyField](EditorGUILayout.PropertyField.html)(m_BooleanProperty);  
      
            // Apply the changes so [Undo](Undo.html)/Redo is working.
            extraDataSerializedObject.ApplyModifiedProperties();  
      
            // Call ApplyRevertGUI to show Apply and Revert buttons.
            ApplyRevertGUI();
        }
    }  
      
    public class BooleanClass : [ScriptableObject](ScriptableObject.html)
    {
        public bool boolean;
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(0, ".boolean")]
    public class BooleanImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            string fileContent = File.ReadAllText(ctx.assetPath);
            var booleanObj = [ObjectFactory.CreateInstance](ObjectFactory.CreateInstance.html)<BooleanClass>();
            if (!bool.TryParse(fileContent, out booleanObj.boolean))
            {
                booleanObj.boolean = false;
            }
            ctx.AddObjectToAsset("main", booleanObj);
            ctx.SetMainObject(booleanObj);
            [Debug.Log](Debug.Log.html)("Imported Boolean value: " + booleanObj.boolean);
        }
    }
    

You can also use ScriptedImporter settings and extraData in the same
AssetImporterEditor:

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.AssetImporters;  
      
    [[CustomEditor](CustomEditor.html)(typeof(SomeScriptedImporter))]
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    public class SomeImporterEditor : [ScriptedImporterEditor](AssetImporters.ScriptedImporterEditor.html)
    {
        // ...  
      
        public override void OnInspectorGUI()
        {
            serializedObject.Update();
            extraDataSerializedObject.Update();  
      
            // Use propertyDrawers and custom [GUI](GUI.html) for any property from both serializedObject and extraDataSerializedObject.  
      
            extraDataSerializedObject.ApplyModifiedProperties();
            serializedObject.ApplyModifiedProperties();  
      
            ApplyRevertGUI();
        }
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(0, ".someFile")]
    public class SomeScriptedImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            // ...
        }
    }
    

### Properties

[extraDataSerializedObject](AssetImporters.AssetImporterEditor-
extraDataSerializedObject.html)| A SerializedObject that represents the
extraDataTarget or the extraDataTargets of the AssetImporterEditor.  
---|---  
[extraDataTarget](AssetImporters.AssetImporterEditor-extraDataTarget.html)|
The extra data object associated with the Editor.target.  
[extraDataTargets](AssetImporters.AssetImporterEditor-extraDataTargets.html)|
An array of objects associated with each Editor.targets.  
[extraDataType](AssetImporters.AssetImporterEditor-extraDataType.html)|
Override this property to return a type that inherits from ScriptableObject.
This makes the AssetImporterEditor aware of serialized data outside of the
Importer.  
[needsApplyRevert](AssetImporters.AssetImporterEditor-needsApplyRevert.html)|
Whether the ApplyRevertGUI method is required to draw in the Inspector.  
[showImportedObject](AssetImporters.AssetImporterEditor-
showImportedObject.html)| Should imported object be shown as a separate
editor?  
[useAssetDrawPreview](AssetImporters.AssetImporterEditor-
useAssetDrawPreview.html)| Determines if the asset preview is handled by the
AssetEditor or the Importer DrawPreview  
  
### Public Methods

[HasModified](AssetImporters.AssetImporterEditor.HasModified.html)| Determine
if the import settings have been modified.  
---|---  
[OnDisable](AssetImporters.AssetImporterEditor.OnDisable.html)| This function
is called when the editor object goes out of scope.  
[OnEnable](AssetImporters.AssetImporterEditor.OnEnable.html)| This function is
called when the object is loaded.  
[OnInspectorGUI](AssetImporters.AssetImporterEditor.OnInspectorGUI.html)|
Override this method to create your own Inpsector GUI for a ScriptedImporter.  
  
### Protected Methods

[Apply](AssetImporters.AssetImporterEditor.Apply.html)| Saves any changes from
the Editor's control into the asset's import settings object.  
---|---  
[ApplyButton](AssetImporters.AssetImporterEditor.ApplyButton.html)| Implements
the 'Apply' button of the inspector.  
[ApplyRevertGUI](AssetImporters.AssetImporterEditor.ApplyRevertGUI.html)|
Add's the 'Apply' and 'Revert' buttons to the editor.  
[Awake](AssetImporters.AssetImporterEditor.Awake.html)| This function is
called when the Editor script is started.  
[CanApply](AssetImporters.AssetImporterEditor.CanApply.html)| Determines if
the modifications to import settings can be applied.  
[InitializeExtraDataInstance](AssetImporters.AssetImporterEditor.InitializeExtraDataInstance.html)|
This method is called during the initialization process of the Editor, after
Awake and before OnEnable.  
[OnApplyRevertGUI](AssetImporters.AssetImporterEditor.OnApplyRevertGUI.html)|
Process the 'Apply' and 'Revert' buttons.  
[RevertButton](AssetImporters.AssetImporterEditor.RevertButton.html)|
Implements the 'Revert' button of the inspector.  
  
### Inherited Members

### Properties

[hasUnsavedChanges](Editor-hasUnsavedChanges.html)| This property specifies
whether the Editor prompts the user to save or discard unsaved changes before
the Inspector gets rebuilt.  
---|---  
[saveChangesMessage](Editor-saveChangesMessage.html)| The message that
displays to the user if they are prompted to save.  
[serializedObject](Editor-serializedObject.html)| A SerializedObject
representing the object or objects being inspected.  
[target](Editor-target.html)| The object being inspected.  
[targets](Editor-targets.html)| An array of all the object being inspected.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[CreateInspectorGUI](Editor.CreateInspectorGUI.html)| Implement this method to
make a custom UIElements inspector.  
---|---  
[CreatePreview](Editor.CreatePreview.html)| Implement this method to make a
custom UIElements inspector preview.  
[DiscardChanges](Editor.DiscardChanges.html)| Discards unsaved changes to the
contents of the editor.  
[DrawDefaultInspector](Editor.DrawDefaultInspector.html)| Draws the built-in
Inspector.  
[DrawHeader](Editor.DrawHeader.html)| Call this function to draw the header of
the editor.  
[DrawPreview](Editor.DrawPreview.html)| The first entry point for Preview
Drawing.  
[GetInfoString](Editor.GetInfoString.html)| Implement this method to show
asset information on top of the asset preview.  
[GetPreviewTitle](Editor.GetPreviewTitle.html)| Override this method if you
want to change the label of the Preview area.  
[HasPreviewGUI](Editor.HasPreviewGUI.html)| Override this method in subclasses
if you implement OnPreviewGUI.  
[OnInteractivePreviewGUI](Editor.OnInteractivePreviewGUI.html)| Implement to
create your own interactive custom preview. Interactive custom previews are
used in the preview area of the inspector and the object selector.  
[OnPreviewGUI](Editor.OnPreviewGUI.html)| Creates a custom preview for the
preview area of the Inspector, the headers of the primary Editor, and the
object selector.You must implement Editor.HasPreviewGUI for this method to be
called.  
[OnPreviewSettings](Editor.OnPreviewSettings.html)| Override this method if
you want to show custom controls in the preview header.  
[RenderStaticPreview](Editor.RenderStaticPreview.html)| Override this method
if you want to render a static preview.  
[Repaint](Editor.Repaint.html)| Redraw any inspectors that shows this editor.  
[RequiresConstantRepaint](Editor.RequiresConstantRepaint.html)| Checks if this
editor requires constant repaints in its current state.  
[SaveChanges](Editor.SaveChanges.html)| Performs a save action on the contents
of the editor.  
[UseDefaultMargins](Editor.UseDefaultMargins.html)| Override this method in
subclasses to return false if you don't want default margins.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[ShouldHideOpenButton](Editor.ShouldHideOpenButton.html)| Returns the
visibility setting of the "open" button in the Inspector.  
---|---  
  
### Static Methods

[CreateCachedEditor](Editor.CreateCachedEditor.html)| On return previousEditor
is an editor for targetObject or targetObjects. The function either returns if
the editor is already tracking the objects, or destroys the previous editor
and creates a new one.  
---|---  
[CreateCachedEditorWithContext](Editor.CreateCachedEditorWithContext.html)|
Creates a cached editor using a context object.  
[CreateEditor](Editor.CreateEditor.html)| Make a custom editor for
targetObject or targetObjects.  
[CreateEditorWithContext](Editor.CreateEditorWithContext.html)| Make a custom
editor for targetObject or targetObjects with a context object.  
[DrawFoldoutInspector](Editor.DrawFoldoutInspector.html)| Draws the inspector
GUI with a foldout header for target.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
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

[HasFrameBounds](Editor.HasFrameBounds.html)| Validates whether custom bounds
can be calculated for this Editor.  
---|---  
[OnGetFrameBounds](Editor.OnGetFrameBounds.html)| Gets custom bounds for the
target of this editor.  
[OnSceneGUI](Editor.OnSceneGUI.html)| Enables the Editor to handle an event in
the Scene view.  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
### Events

[finishedDefaultHeaderGUI](Editor-finishedDefaultHeaderGUI.html)| An event
raised while drawing the header of the Inspector window, after the default
header items have been drawn.  
---|---  
  
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

