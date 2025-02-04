[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-UQuery.html)
  * [中文](/cn/current/Manual/UIE-UQuery.html)
  * [日本語](/ja/current/Manual/UIE-UQuery.html)
  * [한국어](/kr/current/Manual/UIE-UQuery.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-UQuery.html)
  * [中文](/cn/current/Manual/UIE-UQuery.html)
  * [日本語](/ja/current/Manual/UIE-UQuery.html)
  * [한국어](/kr/current/Manual/UIE-UQuery.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Structure UI](UIE-structure-ui.html)
  * [Structure UI with UXML](UIE-UXML.html)
  * Find visual elements with UQuery

[](UIE-LoadingUXMLcsharp.html)

Instantiate UXML from C# scripts

[](UIE-Controls.html)

Structure UI with C# scripts

# Find visual elements with UQuery

You can use [UQuery](../ScriptReference/UIElements.UQuery.html) to find
elements from a [visual tree](UIE-VisualTree.html)An object graph, made of
lightweight nodes, that holds all the elements in a window or panel. It
defines every UI you build with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree). UQuery was inspired by JQuery and
Linq, and is designed to limit dynamic memory allocation. This allows for
optimal performance on mobile platforms.

## Query methods

You can use UQuery through the following extension methods:

  * [`Q`](../ScriptReference/UIElements.UQueryExtensions.Q.html)
  * [`Query`](../ScriptReference/UIElements.UQueryExtensions.Query.html)

Internally, the `Q` and `Query` methods use
[`UQueryBuilder`](../ScriptReference/UIElements.UQueryBuilder_1.html) to
construct a query. These extension methods reduce the verbosity of creating a
`UQueryBuilder`.

To use UQuery to find elements, you must [load](UIE-manage-asset-
reference.html) and [instantiate](UIE-LoadingUXMLcsharp.html) the UXML first,
and then use `Query` or `Q` to construct selection rules on a root **visual
element** A node of a visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement).

`Query` returns a list of elements that match the selection rules. You can
filter the return results of `Query` with the public methods of
[`UQueryBuilder`](../ScriptReference/UIElements.UQueryBuilder_1.html), such as
[First](../ScriptReference/UIElements.UQueryBuilder_1.First.html),
[Last](../ScriptReference/UIElements.UQueryBuilder_1.Last.html),
[AtIndex](../ScriptReference/UIElements.UQueryBuilder_1.AtIndex.html),
[Children](../ScriptReference/UIElements.UQueryBuilder_1.Children.html), and
[Where](../ScriptReference/UIElements.UQueryBuilder_1.Where.html).

`Q` is the shorthand for `Query<T>.First()`. It returns the first element that
matches the selection rules.

## Query elements

You can query elements by their name, their USS class, or their element type
(C# type). You can also query with a predicate or make complex hierarchical
queries.

The following sections use this example UXML to demonstrate how to find
elements:

    
    
    <UXML xmlns="UnityEngine.UIElements">
        <VisualElement name="container1">
          <Button name="OK" text="OK" />
          <Button name="Cancel" text="Cancel" />
        </VisualElement>
         <VisualElement name="container2">
          <Button name="OK" class="yellow" text="OK" />
          <Button name="Cancel" text="Cancel" />
        </VisualElement>
        <VisualElement name="container3">
          <Button name="OK" class="yellow" text="OK" />
          <Button name="Cancel" class="yellow" text="Cancel" />
        </VisualElement>
    </UXML>
    

### Query by name

To find elements by their [name](UIE-USS-Selectors-name.html), use
`Query(name: "element-name")` or `Q(name: "element-name")`. You can omit the
`name` as it’s the first argument. For example:

The following example finds a list of elements named “OK”:

    
    
    List<VisualElement> result = root.Query("OK").ToList();
    

The following example uses `Query` to find the first element named “OK”:

    
    
    VisualElement result = root.Query("OK").First(); //or VisualElement result = root.Q("OK");
    

The following example uses `Q` to find the first element named “OK”:

    
    
    VisualElement result = root.Q("OK");
    

The following example finds the second element named “OK”:

    
    
    VisualElement result3 = root.Query("OK").AtIndex(1);
    

The following example finds the last element named “OK”:

    
    
    VisualElement result4 = root.Query("OK").Last();
    

### Query by USS class

To find elements by a [USS class](UIE-USS-Selectors-class.html), use
`Query(className: "class-name")` or `Q(className: "class-name")`.

The following example finds all the elements that have the class “yellow” and
assigns them to a list:

    
    
    List<VisualElement> result = root.Query(className: "yellow").ToList();
    

The following example finds the first element that has the class “yellow”:

    
    
    VisualElement result = root.Q(className: "yellow");
    

### Query by element type

To find elements by their [element type](UIE-USS-Selectors-type.html)(C#
type), use `Query<Type>` or `Q<Type>`.

The following example finds the first button and adds a tooltip for it:

    
    
    VisualElement result = root.Q<Button>();
    result.tooltip = "This is a tooltip!";
    

The following example finds the third button:

    
    
    VisualElement result = root.Query<Button>().AtIndex(2);
    

**Note** : You can only query by the actual type of the element, not base
classes.

### Query with a predicate

Other than to query elements by name, class, and type, you can also use the
`Where` method to select all elements that satisfy a predicate. The predicate
must be a function callback that takes a single `VisualElement` argument.

The following example finds all the elements with the “yellow” USS class that
have no tooltips:

    
    
    List<VisualElement> result = root.Query(className: "yellow").Where(elem => elem.tooltip == "").ToList();
    

### Complex hierarchical queries

You can combine name, class, and type to make complex hierarchical queries.

The following example finds the first button named “OK” that has a class of
“yellow”:

    
    
    VisualElement result = root.Query<Button>(className: "yellow", name: "OK").First();
    

The following example finds the child cancel button of the “container2”:

    
    
    VisualElement result = root.Query<VisualElement>("container2").Children<Button>("Cancel").First();
    

### Operate on results

You can use the
[ForEach](../ScriptReference/UIElements.UQueryBuilder_1.ForEach.html) method
to operate directly on the query results.

The following example adds a tooltip for any elements that have no tooltips:

    
    
    root.Query().Where(elem => elem.tooltip == "").ForEach(elem => elem.tooltip="This is a tooltip!");
    

## Best practices

Consider the following when you use UQuery:

  * UQuery traverses through the hierarchy to find elements by name, class or type. Cache results from UQuery at initialization.
  * If you need to retrieve multiple elements, use the `QueryState` struct (returned by the `element.Query()` method) and enumerate it to avoid creating lists. You can also construct a query once and execute it on different elements.
  * **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit doesn’t destroy visual elements
that are no longer needed, it uses C# garbage collector to collect them. Be
mindful to not accidentally retain references to visual elements in a class
that outlives the UIDocuments or Window where the elements came from.

  * Capture `VisualElement` variables inside closures.
  * When you create or release lots of elements, enable [incremental garbage collection](performance-incremental-garbage-collection.html) to avoid garbage collector spikes.

## Additional resources

  * [USS selectors](UIE-USS-Selectors.html)
  * [Introduction to visual elements and visual tree](UIE-VisualTree.html)
  * [Load UXML and USS from C# scripts](UIE-manage-asset-reference.html)
  * [Instantiate UXML with C#](UIE-LoadingUXMLcsharp.html)

[](UIE-LoadingUXMLcsharp.html)

Instantiate UXML from C# scripts

[](UIE-Controls.html)

Structure UI with C# scripts

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

