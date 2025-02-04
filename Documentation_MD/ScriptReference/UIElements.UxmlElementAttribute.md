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

# UxmlElementAttribute

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

Declares a custom control.

To create a custom control, you must add the UxmlElement attribute to the
custom control class definition. You must declare the custom control class as
a partial class and inherit it from
[VisualElement](UIElements.VisualElement.html) or one of its derived classes.
When an element is marked with the UxmlElement attribute, a corresponding
[UxmlSerializedData](UIElements.VisualElement.UxmlSerializedData.html) class
is generated in the partial class. This data class contains a
[SerializeField](SerializeField.html) for each field or property that was
marked with the
[UxmlAttributeAttribute](UIElements.UxmlAttributeAttribute.html) attribute.
This serialized data allows for the element to be serialized from UXML and
supports editing in the Attributes field of the Inspector window in the UI
Builder. By default, the custom control appears in the Library tab in UI
Builder. To hide it from the Library tab, provide the
[HideInInspector](HideInInspector.html) attribute.  
  
For an example of migrating a custom control from `UxmlFactory` and
`UxmlTraits` to the `UxmlElement` and `UxmlAttributes` system, refer to
[Enhanced custom controls creation with
UXML](../Manual/UpgradeGuideUnity6#enhanced-custom-controls-creation-with-
uxml.html).  
  
The following example creates a custom control with multiple attributes:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    [UxmlElement]
    public partial class ExampleVisualElement : [VisualElement](UIElements.VisualElement.html)
    {
        [UxmlAttribute]
        public string myStringValue { get; set; }  
      
        [UxmlAttribute]
        public int myIntValue { get; set; }  
      
        [UxmlAttribute]
        public float myFloatValue { get; set; }  
      
        [UxmlAttribute]
        public List<int> myListOfInts { get; set; }  
      
        [UxmlAttribute, UxmlTypeReference(typeof([VisualElement](UIElements.VisualElement.html)))]
        public Type myType { get; set; }  
      
        [UxmlAttribute]
        public [Texture2D](Texture2D.html) myTexture { get; set; }  
      
        [UxmlAttribute]
        public [Color](Color.html) myColor { get; set; }
    }
    

The following UXML document uses the custom control:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <ExampleElement my-string-value="Hello World" my-int-value="123" />
        <ExampleElement my-float-value="3.14" my-list-of-ints="1,2,3" />
        <ExampleElement my-string-value="Hello World" my-int-value="123" />
        <ExampleElement my-texture="project://database/Assets/MyTexture.png" />
        <ExampleElement my-color="#FF0000FF" />
        <ExampleElement my-type="UnityEngine.UIElements.Button, [UnityEngine.UIElementsModule](UnityEngine.UIElementsModule.html)" />
    </ui:UXML>
    

<para>When you create a custom control, the default name used in UXML and UI
Builder is the element type name (C# class name). However, you can customize
the name to make it easier to refer to the element.</para> <para>**Note** :
You are still required to reference the classes' namespace in UXML.</para>
<para>To create a custom name for an element, provide a value to the `name`
property. For example, if you create the following custom button:</para>

    
    
    using UnityEngine.UIElements;  
      
    [UxmlElement("MyButton")]
    public partial class CustomButtonElement : [Button](UIElements.Button.html)
    {
    }
    

You can then reference the custom button in UXML with the custom name or its
type:

    
    
    <ui:UXML xmlns:ui="UnityEngine.UIElements">
        <MyButton />
        <CustomButtonElement />
    </ui:UXML>
    

### Properties

[name](UIElements.UxmlElementAttribute-name.html)|  Provides a custom name for
an element.  
---|---  
  
### Constructors

[UxmlElementAttribute](UIElements.UxmlElementAttribute-ctor.html)|  Exposes a
type of VisualElement to UXML and UI Builder  
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

