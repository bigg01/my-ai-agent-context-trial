# Quick Reference: AI Agent Context

## For Developers

### What You Need to Know

1. **Read `.github/copilot-instructions.md` first** - It tells Copilot how to help you in this project
2. **Copilot learns from it** - Suggestions will match project patterns and conventions
3. **Keep it updated** - As the project evolves, update the context files

### How Copilot Uses Context

- **Code Completions**: Suggests code that follows your patterns
- **Chat Responses**: Answers questions with project context in mind
- **Code Explanations**: Explains code using project-specific terminology
- **Refactoring**: Proposes changes consistent with your architecture

### When to Update Context

Update `.github/copilot-instructions.md` when:
- ✅ You establish new coding patterns
- ✅ Architecture or design changes significantly
- ✅ You adopt new libraries or frameworks
- ✅ Team conventions change
- ✅ New security or performance requirements emerge

### Tips for Effective Context

**Do:**
- ✅ Be specific about your project's unique aspects
- ✅ Include examples of preferred patterns
- ✅ Document common gotchas or pitfalls
- ✅ Explain "why" behind decisions
- ✅ Keep instructions concise and clear

**Don't:**
- ❌ Include generic programming advice
- ❌ Add sensitive information
- ❌ Write overly long explanations
- ❌ Provide conflicting guidance
- ❌ Forget to maintain it

### Example Workflows

#### Starting a New Feature
1. Review copilot-instructions.md for relevant patterns
2. Ask Copilot to help generate boilerplate
3. Use suggestions as a starting point
4. Review and refine generated code

#### Code Review
1. Ask Copilot to explain unfamiliar code
2. Check if code follows project conventions
3. Use Copilot to suggest improvements
4. Verify suggestions align with context

#### Debugging
1. Describe the issue to Copilot
2. Ask for debugging suggestions
3. Request explanations of behavior
4. Get help with testing and validation

### Common Questions

**Q: Does Copilot always follow the instructions?**
A: Copilot uses instructions as guidance but may not always apply them perfectly. Always review suggestions.

**Q: Can I have multiple context files?**
A: The primary file is `.github/copilot-instructions.md`. Additional documentation helps too.

**Q: How specific should instructions be?**
A: Focus on what makes your project unique. Skip generic programming principles.

**Q: What if instructions conflict with code comments?**
A: Copilot considers both. Be consistent across all documentation.

**Q: How often should I update context?**
A: Update when patterns change or after major architectural decisions.

### Testing Your Context

1. Try asking Copilot about project-specific patterns
2. Generate code and check if it follows conventions
3. Use Copilot chat to verify it understands your context
4. Iterate on instructions based on results

### File Structure

```
.github/
├── copilot-instructions.md          # Main instructions for Copilot
├── AI-AGENT-CONTEXT-SPEC.md         # Detailed specification
├── copilot-instructions.template.md  # Template for other projects
└── QUICK-REFERENCE.md                # This file
```

### Related Resources

- [Full Specification](.github/AI-AGENT-CONTEXT-SPEC.md)
- [Project Instructions](.github/copilot-instructions.md)
- [Template for New Projects](.github/copilot-instructions.template.md)
- [GitHub Copilot Docs](https://docs.github.com/copilot)

### Getting Help

- Check the specification document for details
- Review example instructions in this repo
- Consult team leads for project-specific guidance
- Visit GitHub Copilot documentation

---

**Remember**: AI agent context is a living document. Keep it updated, keep it relevant, and keep it helpful!
