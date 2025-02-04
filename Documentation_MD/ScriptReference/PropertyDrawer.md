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

# PropertyDrawer

class in UnityEditor

/

Inherits from:[GUIDrawer](GUIDrawer.html)

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

Base class to derive custom property drawers from. Use this to create custom
drawers for your own Serializable classes or for script variables with custom
[PropertyAttribute](PropertyAttribute.html)s.

PropertyDrawers have two uses:

  * Customize the GUI of every instance of a Serializable class.
  * Customize the GUI of script members with custom [PropertyAttribute](PropertyAttribute.html)s.

If you have a custom Serializable class, you can use a PropertyDrawer to
control how it looks in the Inspector. Consider the Serializable class
Ingredient in the script below:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;  
      
    public enum IngredientUnit { Spoon, Cup, Bowl, Piece }  
      
    // Custom serializable class
    [Serializable]
    public class Ingredient
    {
        public string name;
        public int amount = 1;
        public IngredientUnit unit;
    }  
      
    public class Recipe : [MonoBehaviour](MonoBehaviour.html)
    {
        public Ingredient potionResult;
        public Ingredient[] potionIngredients;
    }
    

Using a custom PropertyDrawer, every appearance of the Ingredient class in the
Inspector can be changed.  
  
You can attach the PropertyDrawer to a Serializable class by using the
[CustomPropertyDrawer](CustomPropertyDrawer.html) attribute and pass in the
type of the Serializable class that it's a drawer for.  
  
You can either use UI Toolkit to build your custom PropertyDrawer or you can
use IMGUI. To create a custom PropertyDrawer using UI Toolkit, you have to
override the
[PropertyDrawer.CreatePropertyGUI](PropertyDrawer.CreatePropertyGUI.html) on
the PropertyDrawer class. To create a custom PropertyDrawer using IMGUI, you
have to override the [PropertyDrawer.OnGUI](PropertyDrawer.OnGUI.html) on the
PropertyDrawer class.  
  
**Note** : You can't run UI Toolkit inside IMGUI. This means if your custom
PropertyDrawer only has a UI Toolkit implementation, it won't work inside an
IMGUI custom Inspector or a parent IMGUI custom PropertyDrawer. Starting from
Unity 2022.2, the default Inspector uses UI Toolkit exclusively in custom
PropertyDrawers. However, you might still need to implement IMGUI if the
property drawers is called from a custom Editor. Prior to 2022.2, it is
recommended that you either implement both IMGUI and UI Toolkit versions of
each PropertyDrawer, or make sure they are exclusively used inside custom UI
Toolkit inspectors.  
  
Here's an example of a custom PropertyDrawer written using UI Toolkit:

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;  
      
    // IngredientDrawerUIE
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(Ingredient))]
    public class IngredientDrawerUIE : [PropertyDrawer](PropertyDrawer.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreatePropertyGUI([SerializedProperty](SerializedProperty.html) property)
        {
            // Create property container element.
            var container = new [VisualElement](UIElements.VisualElement.html)();  
      
            // Create property fields.
            var amountField = new [PropertyField](UIElements.PropertyField.html)(property.FindPropertyRelative("amount"));
            var unitField = new [PropertyField](UIElements.PropertyField.html)(property.FindPropertyRelative("unit"));
            var nameField = new [PropertyField](UIElements.PropertyField.html)(property.FindPropertyRelative("name"), "Fancy Name");  
      
            // Add fields to the container.
            container.Add(amountField);
            container.Add(unitField);
            container.Add(nameField);  
      
            return container;
        }
    }
    

Here's an example of custom PropertyDrawer written using IMGUI. Compare the
look of the Ingredient properties in the Inspector without and with a custom
PropertyDrawer:  
  
![](../StaticFiles/ScriptRefImages/CustomPropertyDrawer_Class.png)  
_Class in the Inspector without (left) and with (right) custom
PropertyDrawer._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    // IngredientDrawer
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(Ingredient))]
    public class IngredientDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        // Draw the property inside the given rect
        public override void OnGUI([Rect](Rect.html) position, [SerializedProperty](SerializedProperty.html) property, [GUIContent](GUIContent.html) label)
        {
            // Using BeginProperty / EndProperty on the parent property means that
            // prefab override logic works on the entire property.
            [EditorGUI.BeginProperty](EditorGUI.BeginProperty.html)(position, label, property);  
      
            // Draw label
            position = [EditorGUI.PrefixLabel](EditorGUI.PrefixLabel.html)(position, [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html)), label);  
      
            // Don't make child fields be indented
            var indent = [EditorGUI.indentLevel](EditorGUI-indentLevel.html);
            [EditorGUI.indentLevel](EditorGUI-indentLevel.html) = 0;  
      
            // Calculate rects
            var amountRect = new [Rect](Rect.html)(position.x, position.y, 30, position.height);
            var unitRect = new [Rect](Rect.html)(position.x + 35, position.y, 50, position.height);
            var nameRect = new [Rect](Rect.html)(position.x + 90, position.y, position.width - 90, position.height);  
      
            // Draw fields - pass [GUIContent.none](GUIContent-none.html) to each so they are drawn without labels
            [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(amountRect, property.FindPropertyRelative("amount"), [GUIContent.none](GUIContent-none.html));
            [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(unitRect, property.FindPropertyRelative("unit"), [GUIContent.none](GUIContent-none.html));
            [EditorGUI.PropertyField](EditorGUI.PropertyField.html)(nameRect, property.FindPropertyRelative("name"), [GUIContent.none](GUIContent-none.html));  
      
            // Set indent back to what it was
            [EditorGUI.indentLevel](EditorGUI-indentLevel.html) = indent;  
      
            [EditorGUI.EndProperty](EditorGUI.EndProperty.html)();
        }
    }
    

The other use of PropertyDrawer is to alter the appearance of members in a
script that have custom [PropertyAttribute](PropertyAttribute.html)s. Say you
want to limit floats or integers in your script to a certain range and show
them as sliders in the Inspector. Using the built-in
[PropertyAttribute](PropertyAttribute.html) called
[RangeAttribute](RangeAttribute.html) you can do just that:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Show this float in the Inspector as a slider between 0 and 10
        [Range(0.0F, 10.0F)]
        public float myFloat = 0.0F;
    }
    

You can make your own [PropertyAttribute](PropertyAttribute.html) as well.
We'll use the code for the [RangeAttribute](RangeAttribute.html) as an
example. The attribute must extend the PropertyAttribute class. If you want,
your property can take parameters and store them as public member variables.

    
    
    // This is not an editor script. The property attribute class should be placed in a regular script file.
    using UnityEngine;  
      
    public class [RangeAttribute](RangeAttribute.html) : [PropertyAttribute](PropertyAttribute.html)
    {
        public float min;
        public float max;  
      
        public [RangeAttribute](RangeAttribute.html)(float min, float max)
        {
            this.min = min;
            this.max = max;
        }
    }
    

Now that you have the attribute, you need to make a PropertyDrawer that draws
properties that have that attribute. The drawer must extend the PropertyDrawer
class, and it must have a [CustomPropertyDrawer](CustomPropertyDrawer.html)
attribute to tell it which attribute it's a drawer for. Here's an example
using IMGUI:

    
    
    // The property drawer class should be placed in an editor script, inside a folder called [Editor](Editor.html).  
      
    // Tell the RangeDrawer that it is a drawer for properties with the [RangeAttribute](RangeAttribute.html).
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof([RangeAttribute](RangeAttribute.html)))]
    public class RangeDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        // Draw the property inside the given rect
        public override void OnGUI([Rect](Rect.html) position, [SerializedProperty](SerializedProperty.html) property, [GUIContent](GUIContent.html) label)
        {
            // First get the attribute since it contains the range for the slider
            [RangeAttribute](RangeAttribute.html) range = attribute as [RangeAttribute](RangeAttribute.html);  
      
            // Now draw the property as a [Slider](UIElements.Slider.html) or an IntSlider based on whether it's a float or integer.
            if (property.propertyType == [SerializedPropertyType.Float](SerializedPropertyType.Float.html))
                [EditorGUI.Slider](EditorGUI.Slider.html)(position, property, range.min, range.max, label);
            else if (property.propertyType == [SerializedPropertyType.Integer](SerializedPropertyType.Integer.html))
                [EditorGUI.IntSlider](EditorGUI.IntSlider.html)(position, property, Convert.ToInt32(range.min), Convert.ToInt32(range.max), label);
            else
                [EditorGUI.LabelField](EditorGUI.LabelField.html)(position, label.text, "Use Range with float or int.");
        }
    }
    

Note that for performance reasons, EditorGUILayout functions are not usable
with PropertyDrawers.  
  
**Note** : Lists and arrays are handled differently with custom drawers. When
the `SerializedProperty` is passed to the `CreatePropertyGUI` method, it
represents each item in the list. However, when the custom drawing is needed
for the list itself, you must wrap the property accordingly.  
  
If you need your property drawer to perform cleanup tasks, such as detaching
itself from editor events, you can implement the
[IDisposable](https://learn.microsoft.com/en-us/dotnet/api/system.idisposable)
interface. This interface allows you to define a method that will be invoked
when the Editor is being destroyed, giving you the opportunity to handle any
necessary cleanup operations.  
  
Additional resources: [PropertyAttribute](PropertyAttribute.html) class,
[CustomPropertyDrawer](CustomPropertyDrawer.html) class.

### Properties

[attribute](PropertyDrawer-attribute.html)| The PropertyAttribute for the
property. Not applicable for custom class drawers. (Read Only)  
---|---  
[fieldInfo](PropertyDrawer-fieldInfo.html)| The reflection FieldInfo for the
member this property represents. (Read Only)  
[preferredLabel](PropertyDrawer-preferredLabel.html)| The label for this
property. (Read Only)  
  
### Public Methods

[CreatePropertyGUI](PropertyDrawer.CreatePropertyGUI.html)| Creates custom GUI
with UI Toolkit for the property.  
---|---  
[GetPropertyHeight](PropertyDrawer.GetPropertyHeight.html)| Override this
method to specify how tall the GUI for this field is in pixels.  
[OnGUI](PropertyDrawer.OnGUI.html)| Override this method to make your own
IMGUI based GUI for the property.  
  
### Inherited Members

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

