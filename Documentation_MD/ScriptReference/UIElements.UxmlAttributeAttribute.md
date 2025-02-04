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

# UxmlAttributeAttribute

class in UnityEngine.UIElements

/

Implemented
in:[UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)

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

Declares that a field or property is associated with a UXML attribute.

You can use the UxmlAttribute attribute to declare that a property or field is
associated with a UXML attribute. When an element is marked with the
UxmlElement attribute, a corresponding
[UxmlSerializedData](UIElements.VisualElement.UxmlSerializedData.html) class
is generated in the partial class. This data class contains a
[SerializeField](SerializeField.html) for each field or property that's marked
with the UxmlAttribute attribute. When a field or property is associated with
a UXML attribute, all of its attributes are transferred over to the serialized
version. This allows for the support of custom property drawers and decorator
attributes, such as [HeaderAttribute](HeaderAttribute.html),
[TextAreaAttribute](TextAreaAttribute.html),
[RangeAttribute](RangeAttribute.html),
[TooltipAttribute](TooltipAttribute.html), and so on.  
  
The following example creates a custom control with custom attributes:

    
    
    using UnityEngine.UIElements;  
      
    namespace Example
    {
        [UxmlElement]
        public partial class MyElement : [VisualElement](UIElements.VisualElement.html)
        {
            [UxmlAttribute]
            public string myStringValue { get; set; }  
      
            [UxmlAttribute]
            public float myFloatValue { get; set; }  
      
            [UxmlAttribute]
            public int myIntValue { get; set; }  
      
            [UxmlAttribute]
            public [UsageHints](UIElements.UsageHints.html) myEnumValue { get; set; }
        }
    }
    

Unity objects can also be UxmlAttributes and will contain a reference to the
asset file when serialized as UXML. The following example creates a custom
control with custom attributes. The types of attributes are UXML template and
texture:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    [UxmlElement]
    public partial class CustomElement : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute]
        public [VisualTreeAsset](UIElements.VisualTreeAsset.html) myTemplate { get; set; }  
      
        [UxmlAttribute]
        public [Texture2D](Texture2D.html) [Texture2D](Texture2D.html) { get; set; }
    }
    

By default, when resolving the attribute name, the field or property name
splits into lowercase words connected by hyphens. The original uppercase
characters in the name are used to denote where the name should be split. For
example, if the property name is `myIntValue`, the corresponding attribute
name would be `my-int-value`. You can customize the attribute name through the
UxmlAttribute name argument. The following example creates a custom control
with customized attribute names:

    
    
    using UnityEngine.UIElements;  
      
    [UxmlElement]
    public partial class CustomAttributeNameExample : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute("character-name")]
        public string myStringValue { get; set; }  
      
        [UxmlAttribute("credits")]
        public float myFloatValue { get; set; }  
      
        [UxmlAttribute("level")]
        public int myIntValue { get; set; }  
      
        [UxmlAttribute("usage")]
        public [UsageHints](UIElements.UsageHints.html) myEnumValue { get; set; }
    }
    

Example UXML:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <CustomAttributeNameExample character-name="Karl" credits="1.23" level="1" usage="DynamicColor" />
    </ui:UXML>
    

If you've changed the name of an attribute and want to ensure that UXML files
with the previous attribute name can still be loaded by UI Builder, use the
`obsoleteNames` argument. This argument matches attributes in the UXML to be
applied to the attribute during serialization. UI Builder uses the new name
when loading the UXML file. The following example creates a custom control
with custom attributes that uses obsolete attribute names:

    
    
    using UnityEngine.UIElements;  
      
    [UxmlElement]
    public partial class CharacterDetails : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute("character-name", "npc-name")]
        public string npcName { get; set; }  
      
        [UxmlAttribute("character-health", "health")]
        public float health { get; set; }
    }
    

The following example UXML uses the obsolete names:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <CharacterDetails npc-name="Haydee" health="100" />
    </ui:UXML>
    

When you create each SerializeField, all attributes are copied across. This
allows you to use decorators and custom property drawers on fields in the UI
Builder. The following example uses a custom control with decorators on its
attribute fields:

    
    
    using UnityEngine.UIElements;
    using UnityEngine;  
      
    [UxmlElement]
    public partial class ExampleText : [VisualElement](UIElements.VisualElement.html)
    {
        [TextArea, UxmlAttribute]
        public string myText;  
      
        [Header("My Header")]
        [Range(0, 100)]
        [UxmlAttribute]
        public int rangedInt;  
      
        [Tooltip("My custom tooltip")]
        [Min(10)]
        [UxmlAttribute]
        public int minValue = 100;
    }
    

The UI Builder displays the attributes with the decorators:  
  
![](../StaticFiles/ScriptRefImages/UIB-decorators.png)  
  
The following example creates a custom control with a custom property drawer:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    public class MyDrawerAttribute : [PropertyAttribute](PropertyAttribute.html) { }  
      
    [UxmlElement]
    public partial class MyDrawerExample : [Button](UIElements.Button.html)
    {
        [UxmlAttribute]
        public [Color](Color.html) myColor;  
      
        [MyDrawer, UxmlAttribute]
        public string myText;
    }
    
    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(MyDrawerAttribute))]
    public class MyDrawerAttributePropertyDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreatePropertyGUI([SerializedProperty](SerializedProperty.html) property)
        {
            var row = new [VisualElement](UIElements.VisualElement.html) { style = { flexDirection = [FlexDirection.Row](UIElements.FlexDirection.Row.html) } };
            var textField = new [TextField](UIElements.TextField.html)("My Text") { style = { flexGrow = 1 } };
            var button = new [Button](UIElements.Button.html) { text = ":" };
            button.clicked += () => textField.value = "RESET";  
      
            // Get the parent property
            var parentPropertyPath = property.propertyPath.Substring(0, property.propertyPath.LastIndexOf('.'));
            var parent = property.serializedObject.FindProperty(parentPropertyPath);  
      
            var colorProp = parent.FindPropertyRelative("myColor");
            textField.TrackPropertyValue(colorProp, p =>
            {
                row.style.backgroundColor = p.colorValue;
            });  
      
            row.style.backgroundColor = colorProp.colorValue;
            row.Add(textField);
            row.Add(button);
            textField.BindProperty(property);  
      
            return row;
        }
    }
    

![](../StaticFiles/ScriptRefImages/UIB-propertydrawer.gif)  
  
You can use struct or class instances as attributes and even lists of struct
or class instances in UXML. However, they must be convertible to and from a
string and you must declare a
[UxmlAttributeConverter<T0>](UIElements.UxmlAttributeConverter_1.html) to
support this conversion. When using the class in a list, ensure that its
string representation does not contain any commas (",") as this character is
used by the list to separate the items. Refer to
[UxmlObjectReferenceAttribute](UIElements.UxmlObjectReferenceAttribute.html)
for an example of a field that supports more complex data. The following
example shows how a class instance can support a property and list:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using UnityEngine.UIElements;  
      
    [Serializable]
    public class MyClassWithData
    {
        public int myInt;
        public float myFloat;
    }  
      
    [UxmlElement]
    public partial class MyElementWithData : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute]
        public MyClassWithData someData;  
      
        [UxmlAttribute]
        public List<MyClassWithData> lotsOfData;
    }
    
    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Globalization;
    using UnityEditor.UIElements;  
      
    public class MyClassWithDataConverter : UxmlAttributeConverter<MyClassWithData>
    {
        public override MyClassWithData FromString(string value)
        {
            // Split using a | so that comma (,) can be used by the list.
            var split = value.Split('|');  
      
            return new MyClassWithData
            {
                myInt = int.Parse(split[0]),
                myFloat = float.Parse(split[1], CultureInfo.InvariantCulture)
            };
        }  
      
        public override string ToString(MyClassWithData value) => FormattableString.Invariant($"{value.myInt}|{value.myFloat}");
    }
    
    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <MyElementWithData some-data="1|2.3" lots-of-data="1|2,3|4,5|6" />
    </ui:UXML>
    

When an attribute shares the same UXML name as an attribute from a child
class, it takes precedence and overrides that field, appearing in the
inspector instead. With this feature, you can substitute a field with a
different type or a custom property. The following example demonstrates how to
replace the IntegerField value with a SliderField.

    
    
    using UnityEngine.UIElements;
    using UnityEngine;  
      
    public class MyOverrideDrawerAttribute : [PropertyAttribute](PropertyAttribute.html) { }  
      
    [UxmlElement]
    public partial class IntFieldWithCustomPropertyDrawer : [IntegerField](UIElements.IntegerField.html)
    {
        // Override the value property to use the custom drawer
        [UxmlAttribute("value"), MyOverrideDrawer]
        internal int myOverrideValue
        {
            get => this.value;
            set => this.value = value;
        }
    }
    
    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.UIElements;
    using UnityEngine.UIElements;  
      
    [[CustomPropertyDrawer](CustomPropertyDrawer.html)(typeof(MyOverrideDrawerAttribute))]
    public class MyOverrideDrawerAttributePropertyDrawer : [PropertyDrawer](PropertyDrawer.html)
    {
        public override [VisualElement](UIElements.VisualElement.html) CreatePropertyGUI([SerializedProperty](SerializedProperty.html) property)
        {
            var field = new [SliderInt](UIElements.SliderInt.html)(0, 100) { label = "Value" };
            field.BindProperty(property);
            return field;
        }
    }
    

### Properties

[name](UIElements.UxmlAttributeAttribute-name.html)|  Provides a custom UXML
name to the attribute.  
---|---  
[obsoleteNames](UIElements.UxmlAttributeAttribute-obsoleteNames.html)|
Provides support for obsolete UXML attribute names.  
  
### Constructors

[UxmlAttributeAttribute](UIElements.UxmlAttributeAttribute-ctor.html)|
Declares that a field or property is associated with a UXML attribute.  
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

